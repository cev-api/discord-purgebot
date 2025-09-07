# Discord Self-Message Deleter

![header](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)
![header](https://img.shields.io/badge/discord.py--self-2.x-magenta?style=flat-square)

A professional, Rich-powered terminal app for browsing your Discord servers and channels, and bulk-deleting your own messages with advanced filters and amazingly advanced UI.

---

## Features
- **Rich terminal UI**: Beautiful tables, panels, and prompts using [Rich](https://github.com/Textualize/rich)
- **ASCII art header** for branding
- **Browse servers and channels** with interactive selection
- **Delete your messages** in any channel, with:
  - Date range filters
  - Keyword filter
  - Option to skip pinned messages
  - Export deleted messages to a file
  - Dry-run/preview mode
  - Progress and confirmation panels
- **Rate limit aware**: Pauses and retries on Discord rate limits

---

## Usage

### 1. Install dependencies
```sh
pip install discord.py-self rich
```

### 2. Get your Discord user token
> **Warning:** Using self-bots is against Discord's Terms of Service and can get your account banned. Use at your own risk and only for educational purposes.

### 3. Configure your token
Edit `purgebot.py` and set your token:
```python
TOKEN = "YOUR_TOKEN_HERE"
```

## Example UI
```
____  _                   _ _____                 
|    \|_|___ ___ ___ ___ _| |  _  |_ _ ___ ___ ___ 
|  |  | |_ -|  _| . |  _| . |   __| | |  _| . | -_|
|____/|_|___|___|___|_| |___|__|  |___|_| |_  |___|
                                          |___|    

Your Servers
┏━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ Index ┃ Server      ┃                 ID ┃
┡━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│     1 │ RealServer  │ 123456789123456789 │
└───────┴─────────────┴────────────────────┘

Channels in RealServer
┏━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┓
┃ Index ┃ Channel              ┃ Type ┃
┡━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━┩
│     1 │ general              │ text │
│     2 │ off-topic            │ text │
└───────┴──────────────────────┴──────┘
Enter channel number: 2

Delete messages after date (YYYY-MM-DD, blank for none):
Delete messages before date (YYYY-MM-DD, blank for none):
Only delete messages containing keyword (blank for none):
Skip pinned messages? (Y/n):
Export deleted messages to file (filename or blank for none):
How many of your last messages to delete? (leave blank for all):

╭─────────────────────────────────────────────────  Confirm Deletion ──────────────────────────────────────────────────╮
│ About to delete up to all messages from off-topic with filters:                                                      │
│ After: None, Before: None, Keyword: None, Skip pinned: True, Export: None                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Proceed? (Y/N):

```

---

## Disclaimer
- This project is for educational and personal use only.
- **Using self-bots is against Discord's Terms of Service and can result in account termination.**
- The author is not responsible for any misuse or account bans.

