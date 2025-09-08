# Discord Purge - Bulk Delete Your Own Messages!

![header](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)
![header](https://img.shields.io/badge/discord.py--self-2.x-magenta?style=flat-square)

![Purge](https://i.imgur.com/rt0Y4vF.png)

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


## Disclaimer
- This project is for educational and personal use only.
- **Using self-bots is against Discord's Terms of Service and can result in account termination.**
- I am not responsible for any misuse or account bans.
- No guarantee of success in deleting everything you plan or want to delete

