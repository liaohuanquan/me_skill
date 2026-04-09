#!/usr/bin/env python3
"""
微信消息采集器 (WeChat Collector)

支持的来源格式：
1. 解密后的 SQLite 数据库 (Msg.db) —— 适合使用 PyWxDump 等工具解密后的数据库
2. WeChatMsg (留痕) 导出的 JSON 格式
3. 通用 CSV 导出格式 (包含 Nickname, Message, StrTime 等字段)

用法：
    # 解析 SQLite 数据库 (需要指定目标主体的 Nickname 或备注)
    python wechat_collector.py --db Msg.db --target "我的昵称" --output output.txt
    
    # 解析 WeChatMsg 导出的 JSON
    python wechat_collector.py --json messages.json --target "我的昵称" --output output.txt
"""

import sqlite3
import json
import csv
import argparse
import sys
from pathlib import Path

def parse_sqlite(db_path, target_name):
    """从解密后的微信 SQLite 数据库中提取消息"""
    if not Path(db_path).exists():
        print(f"错误: 数据库文件不存在 {db_path}", file=sys.stderr)
        return []

    messages = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # 尝试查询消息表。微信的表结构较复杂，这里使用通用的提取逻辑。
        # 注意：不同版本的微信数据库表名和字段可能略有差异。
        # 典型的消息存储在 MSG 表中，type=1 通常是文本消息。
        # 我们假设用户已经使用了 PyWxDump 等工具提取出了结构化的视图或表。
        
        # 检查是否存在典型的 MSG 表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='MSG';")
        if not cursor.fetchone():
            # 尝试另一种常见的表名或视图
            query = "SELECT TalkerId, StrContent, StrTime FROM ChatMsg WHERE IsSender = 1"
        else:
            # 标准 Msg.db 结构（简化版逻辑）
            query = """
            SELECT TalkerId, StrContent, StrTime 
            FROM MSG 
            WHERE IsSender = 1 AND Type = 1
            """
            
        cursor.execute(query)
        rows = cursor.fetchall()
        
        for row in rows:
            # row: (talker_id, content, time)
            content = row[1]
            if not content or content.startswith("<msg>"): # 过滤 XML 格式的系统/特殊消息
                continue
                
            messages.append({
                "sender": target_name, # 既然是采集“自己”，通常过滤的是 IsSender=1
                "content": content.strip(),
                "timestamp": row[2]
            })
        
        conn.close()
    except Exception as e:
        print(f"解析 SQLite 出错: {e}", file=sys.stderr)
        
    return messages

def parse_wechat_json(json_path, target_name):
    """解析 WeChatMsg 导出的 JSON 格式"""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    messages = []
    # 兼容 WeChatMsg 的多种 JSON 结构
    raw_msgs = data if isinstance(data, list) else data.get("messages", [])
    
    for msg in raw_msgs:
        # WeChatMsg 通常通过 is_sender 标识是否为本人
        is_self = msg.get("is_sender") == 1 or msg.get("IsSender") == 1
        if not is_self:
            continue
            
        content = msg.get("content") or msg.get("StrContent") or ""
        # 过滤表情包 [表情] 和图片消息
        if not content or "[表情]" in content or "[图片]" in content:
            continue
            
        messages.append({
            "sender": target_name,
            "content": content.strip(),
            "timestamp": msg.get("time") or msg.get("StrTime") or ""
        })
    return messages

def format_output(messages):
    """格式化为分析可用的内容"""
    lines = ["# 微信原始消息汇总", "---", ""]
    
    # 区分长内容（更有价值的观点）和短回复
    long_msgs = [m for m in messages if len(m["content"]) > 30]
    short_msgs = [m for m in messages if len(m["content"]) <= 30]
    
    lines.append("## 核心表达与深度交流")
    for m in long_msgs:
        ts = f"[{m['timestamp']}] " if m['timestamp'] else ""
        lines.append(f"{ts}{m['content']}")
        lines.append("")
        
    lines.append("---")
    lines.append("## 日常沟通片段")
    for m in short_msgs[:200]: # 日常片段取样
        ts = f"[{m['timestamp']}] " if m['timestamp'] else ""
        lines.append(f"{ts}{m['content']}")
        
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="微信消息提取工具")
    parser.add_argument("--db", help="解密后的 Msg.db 路径")
    parser.add_argument("--json", help="WeChatMsg 导出的 JSON 路径")
    parser.add_argument("--target", default="Me", help="分身名称")
    parser.add_argument("--output", help="输出 TXT 路径")
    
    args = parser.parse_args()
    
    messages = []
    if args.db:
        messages = parse_sqlite(args.db, args.target)
    elif args.json:
        messages = parse_wechat_json(args.json, args.target)
    else:
        print("请提供 --db 或 --json 输入源")
        sys.exit(1)
        
    if not messages:
        print("未提取到任何有效消息")
        return
        
    content = format_output(messages)
    
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"已提取 {len(messages)} 条消息到 {args.output}")
    else:
        print(content)

if __name__ == "__main__":
    main()
