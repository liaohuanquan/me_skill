# Me.Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)


> *"You AI guys are traitors to the codebase — you've already killed frontend, now you're coming for backend, QA, ops, infosec, chip design, and eventually yourselves and all of humanity"*

Welcome to your personal digital life backup plan. If you find yourself drained by endless meetings, repetitive documentation, or exhausting Code Reviews, it’s time to clone yourself.

This project enables you to compress your own coding habits, analytical frameworks, complaint patterns, and debugging intuition into a localized AI Skill. When you want to check out for the day, let `Me.Skill` pick up the slack.

## Why Distill Yourself?

- **Clone Your Coding OCD**: Tired of reviewing messy code? Feed your conventions to your clone. It will review PRs on your behalf, criticizing bad code in your exact tone of voice.
- **Cyber Slices of Experience**: Solved a mind-boggling architectural nightmare today? Tell your twin. The next time a similar issue arises, it will remember better than you do.
- **Replicate Your Office Persona**: We don't just want an AI that codes. We want a digital twin that frowns at bad requirements, defends its architecture gracefully, and expertly shifts blame when necessary.

## How It Works

The clone operates on a unique **Two-Layer Architecture**:

1. **Persona Engine**: This is your social defense mechanism. By analyzing your chat logs and emails, it learns your buzzwords, catchphrases, emoji habits, and how you naturally push back against scope creep.
2. **Work Skill Core**: This is your professional brain. It digests your technical specs, Wiki documents, and past output to map out your technical boundaries and specific stack expertise.

Whenever assigned a task, **the Persona Engine first decides the "attitude," then the Work Skill Core builds the technical solution.**

## Usage Guide

### 1. Environment Setup
Install dependencies in the project root:
```bash
pip install -r requirements.txt
```

### 2. Guided Creation
In Claude Code or similar environments, type:
```bash
/create-myskill
```
Simply answer 3 questions (Codename, Basic Info, Personality) and then choose your data sources.

### 3. Providing "Soul" Materials
The system supports:
*   **Auto-Collection**: Pull your personal Feishu/DingTalk message history and documents.
*   **File Import**: Upload your PRDs, tech specs, or Code Review comments.
*   **Direct Paste**: Any text that captures your thinking logic or speaking style.

### 4. Summoning Your Twin
Once created, invoke your twin using its codename (slug):
*   `/{slug}`: Full Twin (Tone + Technical solution)
*   `/{slug}-work`: Technical Core only
*   `/{slug}-persona`: Personality simulation only

### 5. Continuous Evolution
If the twin doesn't act like you, correct it directly:
> "I wouldn't reply like this; I'm usually more direct..."

The system learns in real-time through the **Correction layer** to tighten its performance.

Don't let your hard-earned experience fade away. Back up the best version of yourself today.
