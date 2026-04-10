<div align="center">

# 自己.skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

[English Version](README_EN.md)

> *"你们搞大模型的就是码奸，你们已经害死前端兄弟了，还要害死后端兄弟，测试兄弟，运维兄弟，害死网安兄弟，害死ic兄弟，最后害死自己害死全人类"*

</div>

欢迎来到属于你的“数字生命备份计划”。当你被无穷无尽的会议、重复的文档编写或是恼人的 Code Review 彻底淹没时，也许你需要一个完全懂你、随时在线的替身。

这个项目能把你自己的代码习惯、思维框架、吐槽模式乃至排错直觉，全部打包、蒸馏进一个本地化的 AI Skill 里。当你想下班时，让这个“自己.skill”代你出击。

## 为什么你需要蒸馏自己？

- **完美模仿你的代码洁癖**：受够了别人乱写代码？把你的规范喂给分身，让它代替你在 PR 里指点江山，连语气都跟你一模一样。
- **经验的赛博切片**：今天解决了一个极其刁钻的神仙 Bug？立刻告诉你的分身。下次遇到类似问题，它比你的记忆还可靠。
- **复刻你的职场人设**：我们不只要一个能写代码的 AI，我们要的是一个遇到烂需求会皱眉、被质问会反击（或甩锅）的数字分身。

## 它是怎么运作的？

分身系统拥有独特的**双层架构（Two-Layer Architecture）**：

1. **性格引擎 (Persona)**：它是你的对外防御机制。它能通过分析你过往的聊天记录，学会你的高频词库、口头禅、emoji 偏好，以及你“如何拒绝不合理需求”、“如何向上管理”。
2. **专业内核 (Work Skill)**：它是你的干货大脑。从你编写的系统架构、Wiki 文档和历史代码中，提取你负责的业务边界和技术储备。

每次面临任务，它会**先由性格引擎判断用什么样的态度接招，再由专业内核组合出技术上的答案。**

## 使用指南

### 1. 安装环境
在项目根目录下安装依赖：
```bash
pip install -r requirements.txt
```

### 2. 引导式创建
在 Claude Code 或类似环境中输入：
```bash
/create-myskill
```
只需回答 3 个问题（代号、基本信息、性格倾向），然后选择你的数据来源（飞书/钉钉自动拉取或手动上传）。

### 3. 提供“灵魂”素材

为了让分身更像你，建议提供尽可能丰富的原材料。系统支持以下来源：

| 来源 | 聊天记录 | 文档 / 知识库 | 备注 |
| :--- | :---: | :---: | :--- |
| **微信 (WeChat)** | ✅ SQLite / JSON | — | 支持解密数据库或 WeChatMsg 导出 |
| **飞书 (Feishu)** | ✅ API / JSON | ✅ Wiki / 文档 | 推荐使用自动采集脚本 |
| **钉钉 (DingTalk)** | ✅ 浏览器采集 | ✅ 知识库 | 钉钉 API 限制较多 |
| **工作文件** | ✅ | ✅ PDF / MD | 你的 PRD、架构图、周报等 |
| **其他** | ✅ 邮件 / 录音 | — | 支持 .eml 及图片截图 |

系统工具：
*   **自动采集**：拉取你本人的飞书/钉钉历史消息和文档。
*   **微信导入**：通过 `tools/wechat_collector.py` 导入解密后的数据库或 JSON 导出文件。
*   **文件导入**：你写的 PRD、技术方案、Code Review 评论。
*   **直接粘贴**：任何能体现你思考逻辑和说话口吻的文字。

### 4. 召唤分身
创建完成后，使用你的代号（slug）即可调用：
*   `/{slug}`：完整分身（语气+技术方案）
*   `/{slug}-work`：纯技术内核
*   `/{slug}-persona`：纯性格模拟

### 5. 持续进化
若分身表现不像你，直接纠正它：
> “我不会这样回复，我通常会更直接一点……”

系统会通过 **Correction (纠正层)** 实时学习并收敛分身表现。

别让你的宝贵经验随着岁月流逝，趁现在，把最好的自己存下来吧。

## 开源许可

本项目采用 [MIT License](LICENSE) 许可协议。

