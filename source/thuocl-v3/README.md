# THUOCL 中文试用包 v3

固定THUOCL提交a30ce79d895d01ab5132a5c74c29703ff7efb4cc；原始11类数据、DF和MIT许可完整保留。153175个原生词语—拼音组合，补充分值-3。保留v2的20项上下文注音修正，新增33项明确中文读法的数字词（如32位、蓝牙4.0、从0到1），不把THUOCL的DF当作libime语言模型频率。

这33项保留原词形，可输入中文读音选择，已在真实libime中逐条验证候选、选择、学习和后续输入。不是任意字母数字串的自动拼音转换。source/numeric-readings.tsv记载读音和复核范围；其余多数词条仍为pypinyin0.55.0机器注音，不称全部人工审核。

153175条编译后全文回转一致；197组日常输入对比v2名次无变化，20项上下文修正候选名次保留。3114条英文、混合词或特殊原文尚未编码，见source/unsupported.tsv。不能称THUOCL全量混输接入。引擎共享混输是独立功能，不依赖本包。

按需下载，不内置。应用支持更新已知公共原版，保留启停状态；个人修改版不会自动覆盖，卸载公共包不应删除个人学习。旧包仍保留。

重建：pypinyin==0.55.0；python tools/prepare_thuocl.py --source source/upstream --output rebuilt --corrections source/reading-corrections.tsv --numeric-readings source/numeric-readings.tsv；libime_pinyindict rebuilt/thuocl-cn.txt thuocl-cn.dict。

THUOCL源文件MIT；20项选用雾凇读音注释遵GPL-3.0；新增数字读音按THUOCL上下文明确复核，非官方音频证明。未做Android设备验收。
