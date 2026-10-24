#!/usr/bin/env python3
"""Prepare all 11 THUOCL categories for libime, with explicit machine-reading status.

DF remains source metadata, never a replacement for the core language model score.
The native supplement uses a tested fixed -3 score and is opt-in.
"""
import argparse
import csv
import json
from pathlib import Path
import re

REVISION = 'a30ce79d895d01ab5132a5c74c29703ff7efb4cc'
NATIVE_SCORE = -3
CATEGORIES = ('IT', 'animal', 'caijing', 'car', 'chengyu', 'diming', 'food',
              'law', 'lishimingren', 'medical', 'poem')

def read_source(path):
    for number, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        if not line.strip():
            continue
        fields = line.split('\t')
        if len(fields) != 2 or not fields[0].strip():
            raise ValueError(f'{path.name}:{number}: unexpected source format')
        word, raw_df = (field.strip() for field in fields)
        yield {'word': word, 'rawDF': raw_df, 'df': int(raw_df) if raw_df.isdigit() else None,
               'category': path.stem.removeprefix('THUOCL_'), 'line': number}

def prepare(source, output, reading, corrections=None, numeric_readings=None):
    corrections = corrections or {}
    numeric_readings = numeric_readings or {}
    for word, entry in numeric_readings.items():
        if (not re.fullmatch(r'[\u3400-\u9fff0-9.]+', word) or not re.search(r'[0-9]', word)
                or not re.search(r'[\u3400-\u9fff]', word)
                or not re.fullmatch("[a-z]+(?:'[a-z]+)*", entry.get('pinyin',''))
                or not entry.get('reason','').strip()):
            raise ValueError(f'Invalid reviewed numeric reading: {word}')
    # Fail before writing output if a category is missing.
    rows = [row for category in CATEGORIES
            for row in read_source(source/'data'/f'THUOCL_{category}.txt')]
    entries = {}; unsupported = []; invalid_df = 0; duplicates = 0
    for row in rows:
        invalid_df += row['df'] is None
        word = row['word']
        numeric = word in numeric_readings
        if not re.fullmatch('[\u3400-\u9fff]+', word) and not numeric:
            unsupported.append({**row, 'reason': 'non-Han or internal whitespace; original retained'})
            continue
        pinyin = numeric_readings[word]["pinyin"] if numeric else corrections[word]["pinyin"] if word in corrections else "'".join(reading(word))
        if not re.fullmatch("[a-z]+(?:'[a-z]+)*", pinyin) or (not numeric and len(pinyin.split("'")) != len(word)):
            unsupported.append({**row, 'reason': 'unresolved machine reading; original retained'})
            continue
        key = word, pinyin
        if key in entries:
            duplicates += 1
        entries.setdefault(key, []).append(row)
    output.mkdir(parents=True, exist_ok=True)
    with (output/'thuocl-cn.txt').open('w', encoding='utf-8', newline='\n') as stream:
        for word, pinyin in sorted(entries):
            stream.write(f'{word} {pinyin} {NATIVE_SCORE}\n')
    with (output/'unsupported.tsv').open('w', encoding='utf-8', newline='') as stream:
        fields = ['word', 'rawDF', 'df', 'category', 'line', 'reason']
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', lineterminator='\n')
        writer.writeheader(); writer.writerows(unsupported)
    with (output/'source-records.jsonl').open('w', encoding='utf-8', newline='\n') as stream:
        for (word, pinyin), provenance in sorted(entries.items()):
            stream.write(json.dumps({'word': word, 'pinyin': pinyin, 'readingStatus': 'context-reviewed-numeric-reading' if word in numeric_readings else 'context-reviewed-source-aligned' if word in corrections else 'machine-inferred',
                                     'readingEvidence': numeric_readings.get(word, corrections.get(word)),
                                     'sources': provenance}, ensure_ascii=False)+'\n')
    report = {'upstream': 'https://github.com/thunlp/THUOCL', 'revision': REVISION,
              'categories': len(CATEGORIES), 'sourceRows': len(rows), 'nativeEntries': len(entries),
              'duplicateKeys': duplicates, 'unsupportedRows': len(unsupported), 'invalidDFRows': invalid_df,
              'humanPronunciationReviewed': False,
              'contextReadingCorrections': len({word for word, _ in entries if word in corrections}),
              'numericReadingEntries': len({word for word, _ in entries if word in numeric_readings}), 'nativeScore': NATIVE_SCORE, 'defaultEnabled': False,
              'nativeRankingVerified': False}
    (output/'report.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    return report

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--corrections', type=Path)
    parser.add_argument('--numeric-readings', type=Path)
    args = parser.parse_args()
    corrections = {row['word']: row for row in csv.DictReader(args.corrections.read_text(encoding='utf-8-sig').splitlines(), delimiter='\t')} if args.corrections else None
    numeric = {row['word']: row for row in csv.DictReader(args.numeric_readings.read_text(encoding='utf-8-sig').splitlines(), delimiter='\t')} if args.numeric_readings else None
    from pypinyin import lazy_pinyin, Style
    result = prepare(args.source, args.output, lambda word: lazy_pinyin(word, style=Style.NORMAL, strict=True), corrections=corrections, numeric_readings=numeric)
    print(json.dumps(result, ensure_ascii=False, indent=2))
