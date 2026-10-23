#!/usr/bin/env python3
"""Select declared Rime source keys from the prior native roundtrip, preserving decoder weights."""
import argparse,json
from pathlib import Path

def prepare(source,native,out):
 keys={}
 body=False
 for line in source.read_text(encoding='utf-8-sig').splitlines():
  if line.strip()=='...':body=True;continue
  if not body or not line.strip() or line.lstrip().startswith('#'):continue
  fields=line.split('\t')
  if len(fields)<2:raise ValueError('Invalid Rime row')
  word=fields[0].strip();pinyin="'".join(fields[1].split())
  keys[(word,pinyin)]=None
 installed={}
 for line in native.read_text(encoding='utf-8').splitlines():
  if not line.strip():continue
  word,pinyin,weight=line.rsplit(maxsplit=2)
  installed[(word,pinyin)]=weight
 selected={k:weight for k,weight in installed.items() if k in keys}
 missing=[{'word':k[0],'pinyin':k[1],'reason':'Not present in prior native roundtrip; requires converter audit, not assigned a fabricated weight.'} for k in keys if k not in installed]
 out.mkdir(parents=True,exist_ok=True)
 (out/'modern-cn.txt').write_text(''.join(f'{word} {pinyin} {weight}\n' for (word,pinyin),weight in selected.items()),encoding='utf-8',newline='\n')
 (out/'unmapped.json').write_text(json.dumps(missing,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 report={'sourceUniqueKeys':len(keys),'priorNativeEntries':len(installed),'retainedEntries':len(selected),'excludedNonSourceEntries':len(installed)-len(selected),'unmappedEntries':len(missing),'existingNativeWeightsPreserved':True}
 (out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 return report

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for name in ('source','native','out'):p.add_argument('--'+name,type=Path,required=True)
 a=p.parse_args();print(json.dumps(prepare(a.source,a.native,a.out),ensure_ascii=False))
