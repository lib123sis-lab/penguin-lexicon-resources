# THUOCL 中文试用包 v2

固定THUOCL提交a30ce79d895d01ab5132a5c74c29703ff7efb4cc，原始11类文件、DF及MIT许可完整保留。153142个原生词语—拼音组合，补充分值仍为-3，不改变语言模型或个人学习。

在原有机器注音基础上，20个常用IT上下文词经语言复核并与固定雾凇已有注音对齐，纠偏原因/固定来源在source/reading-corrections.tsv；仅这20词标记context-reviewed-source-aligned，其余仍machine-inferred，不能称全部人工终审。读音整理注释沿用GPL-3.0，THUOCL原文件仍MIT。

真实libime1.1.12编译与153142条全文回转一致；197日常输入对比旧包名次变化0。20项正确输入前后均前20，名次相同，不声称首选率提高；二进制移除20个旧错误注音键，错误输入仍可能经其它候选路径出现相同词。

3147条英文/中英混合/数字/标点等依旧未编码：原始内容保存在source/unsupported.tsv。这是中文试用包，不是THUOCL全量混输引擎；不要把无法使用的原始行计为已安装原生词条。

按需下载、不内置；已有普通包需保留个人修改版本后手动替换公共包。重建：libime_pinyindict source/thuocl-cn.txt thuocl-cn.dict。或以随包原始源及pypinyin0.55.0运行tools/prepare_thuocl.py --source source/upstream --output rebuilt --corrections source/reading-corrections.tsv，再编译原生。无Android设备验收。
