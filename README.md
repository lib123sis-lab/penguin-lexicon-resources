# 小企鹅输入法词库资源

仅分发可选中文词库、相应来源与许可；不含输入法私有源码、角色、密钥或个人数据。基础Fcitx5/libime中文词库仍内置，不在这里发布。

## 下载与导入

[统一词库下载页](https://github.com/lib123sis-lab/penguin-lexicon-resources/releases/tag/lexicons-v2)每种词库只保留一个当前完整包，无需下载旧版。建议在合适、稳定的网络环境里下载。输入法设置→词库与语言资源→相应分类，下载后导入；当前版本首次安装启用，已有词库更新保留启停和个人编辑。

|词库|当前完整下载|真实范围|
|---|---|---|
|日常词库|[daily-v1.zip](https://github.com/lib123sis-lab/penguin-lexicon-resources/releases/download/lexicons-v1/daily-v1.zip)|529条|
|雾凇拼音（固定版）|[rime-ice-v2.zip](https://github.com/lib123sis-lab/penguin-lexicon-resources/releases/download/lexicons-v1/rime-ice-v2.zip)|固定版543117条；1个不支持音节随包说明|
|统一游戏词库 v3|[unified-games-v3.zip](https://github.com/lib123sis-lab/penguin-lexicon-resources/releases/download/lexicons-v1/unified-games-v3.zip)|洛克王国：世界506条、战双帕弥什625条|
|THUOCL 中文试用包|[thuocl-preview-v3.zip](https://github.com/lib123sis-lab/penguin-lexicon-resources/releases/download/lexicons-v1/thuocl-preview-v3.zip)|153175条中文试用；多数读音机器推断，3114项混合/特殊原文未编码|
|音乐词库|[music-v1.zip](https://github.com/lib123sis-lab/penguin-lexicon-resources/releases/download/lexicons-v1/music-v1.zip)|5466个词语—拼音组合|
|个人专业词库（公共主题词表）|[professional-v1.zip](https://github.com/lib123sis-lab/penguin-lexicon-resources/releases/download/lexicons-v1/professional-v1.zip)|公共主题词表1004条，不含个人学习数据|
|热词|[hotwords-v2.zip](https://github.com/lib123sis-lab/penguin-lexicon-resources/releases/download/lexicons-v1/hotwords-v2.zip)|141条历史与现代精选；不是逐年完整百年全集|
|搜狗精选词库（成语与地名扩展）|[sogou-v2.zip](https://github.com/lib123sis-lab/penguin-lexicon-resources/releases/download/lexicons-v2/sogou-v2.zip)|节日44、财务418、成语俗语与地名49379，共49841词语—拼音组合；不是全站镜像|

## 许可和验证边界

各ZIP附源词表、原生输入、来源/许可和验证说明。THUOCL固定源thunlp/THUOCL遵守MIT，精选读音标注按包内GPL-3.0说明；雾凇遵守iDvel/rime-ice GPL-3.0。搜狗首批在用户于2026-10-24明确确认取得分发许可后发布，保留原始SCEL与官方来源说明。其余包逐项说明见包内文件及source目录；不改变相应商标和游戏素材权利。

维基百科、维基文库、维基词典在输入法维基词库页分别提供，来自[fcitx5-pinyin-zhwiki 0.3.0](https://github.com/felixonmars/fcitx5-pinyin-zhwiki/releases/tag/0.3.0)，遵守CC-BY-SA-4.0署名要求。

条数是实际已编译词语—拼音组合，不等同于每个简称首选、语音热词或人工逐词终审。主机libime验证不代替设备验收。旧源码和版本记录留在Git历史，当前Release不再并列过期ZIP。应用保留旧包识别信息，个人编辑不自动覆盖。
