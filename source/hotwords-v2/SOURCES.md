历史来源与审核依据见source/historical-approved.tsv及source/source-records.json；12项按用户批准纳入，不伪称独立核验。以下保留既有现代精选来源记录。

# 中文词库与热词来源

词库是拼音候选的补充，不改变离线语音模型的词汇表，也不虚构手写识别结果。

- 通用词库：Rime Ice / 雾凇拼音，https://github.com/iDvel/rime-ice ，固定提交 `da1fbe602e38f26db846fa10120ee64c2b0324c0` 的 `cn_dicts/base.dict.yaml`。原文件保留其来源和版权说明，附 GPL-3.0 许可。二进制是使用 libime_pinyindict 转换的独立词库数据文件。
- 2022：https://www.cp.com.cn/Content/2022/12-20/2040492815.html ；https://paper.people.com.cn/rmlt/html/2023-02/20/content_25984584.htm 。
- 2023：https://news.cctv.cn/2023/12/20/ARTIdiL3N6DaFWHPkCV2btGi231220.shtml ；https://www.moe.gov.cn/jyb_xwfb/s5147/202312/t20231218_1095016.html ；https://news.youth.cn/jsxw/202312/t20231205_14945078.htm 。
- 2024：https://www.cp.com.cn/Content/2024/12-17/1502526588.html ；https://www.cp.com.cn/Content/2024/12-20/1342042638.html ；https://www.thepaper.cn/newsDetail_forward_29761750 。
- 2025：https://nlp.ccnu.edu.cn/news/149 ；https://paper.people.com.cn/fcyym/pad/content/202512/26/content_30133212.html 。
- 2026（截至本次整理，非全年榜单）：https://www.news.cn/tech/20260315/67f344298af24b9290f36295bb29924d/c.html ；https://www.cac.gov.cn/2026-05/08/c_1779979789523320.htm ；https://www.samr.gov.cn/bzjss/tzgg/art/2026/art_bbf820423744486192f890d32ec07764.html 。

年份标注其参考榜单或报道年份，不表示每个词都是当年第一次出现，也不代表收录了全部网络热词。人工校对的 56 项词条与拼音见 `hotwords.tsv`，转换与词频处理见 `build_dictionary.py`，原始字典及准确数量、哈希见 `original/` 与 `BUILD-INFO.json`。

手写和快捷操作参考 Google Gboard 官方文档：https://support.google.com/gboard/answer/9108773?hl=en ，https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin 。停笔识别、滑动候选、展开候选及面板内空格滑动光标由本项目实现；Fcitx 原有的拼音键盘空格滑动光标、编辑和剪贴板功能保留。

## v0.4.1 个人主题补充词库

416 条按用户常用话题人工选定的词汇：哲学与思想史、宗教学与阅读、学习考研、数码隐私、出行日常。详见 personal-vocabulary.tsv。不是近五年热词的完整统计；原有热词和通用词库均保留。没有加入账号、邮箱、学号或健康记录。

## v0.4.2 日常表达

新增日常交流短语和显式候选首位规则。名单为人工选取，未声称统计语料覆盖率；保留此前416条个人主题词库。新规则在首次启动合并到自定义短语，保留用户已有同码词条和手工置顶。
