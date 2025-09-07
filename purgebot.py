import discord
import asyncio
import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

TOKEN = "YOUR_TOKEN_HERE"  # Replace with your Discord account token
client = discord.Client(self_bot=True)
console = Console()

ASCII_HEADER = r'''[bold magenta]
 ____  _                   _ _____                
|    \|_|___ ___ ___ ___ _| |  _  |_ _ ___ ___ ___ 
|  |  | |_ -|  _| . |  _| . |   __| | |  _| . | -_|
|____/|_|___|___|___|_| |___|__|  |___|_| |_  |___|
                                By CevAPI |___| v1.0   
[/bold magenta]'''

def get_input(prompt, default=None):
    try:
        return input(prompt)
    except EOFError:
        return default

def parse_date(date_str):
    try:
        return datetime.datetime.fromisoformat(date_str)
    except Exception:
        return None

async def delete_own_messages(channel, limit=None, dry_run=False, after=None, before=None, keyword=None, skip_pinned=True, export_file=None):
    print(f"\nProcessing messages in #{channel.name}...")
    count = 0
    deleted = 0
    failed = 0
    exported = []
    # Set limit=None to fetch all messages
    async for msg in channel.history(limit=limit, after=after, before=before, oldest_first=True):
        if msg.author.id != client.user.id:
            continue
        if skip_pinned and getattr(msg, "pinned", False):
            continue
        if keyword and keyword.lower() not in msg.content.lower():
            continue
        count += 1
        print(f"Found: [{msg.created_at}] {msg.content}")
        exported.append(f"[{msg.created_at}] {msg.content}")
        if not dry_run:
            while True:
                try:
                    await msg.delete()
                    print(f"Deleted: [{msg.created_at}] {msg.content}")
                    deleted += 1
                    await asyncio.sleep(0.5)
                    break
                except discord.errors.HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(f"Rate limited. Pausing for {retry_after} seconds before retrying this message...")
                        await asyncio.sleep(retry_after)
                        # After waiting, retry the same message
                    else:
                        print(f"Failed to delete: {e}")
                        failed += 1
                        break
        if limit and deleted >= limit:
            break
    print(f"Processed {count} messages, deleted {deleted}, failed {failed}.")
    if export_file and exported:
        with open(export_file, "a", encoding="utf-8") as f:
            for line in exported:
                f.write(line + "\n")
        print(f"Exported deleted messages to {export_file}")

async def delete_all_own_messages_in_guild(guild, **kwargs):
    print(f"\nDeleting your messages from all channels in {guild.name}...")
    total_deleted = 0
    for channel in guild.text_channels:
        print(f"\nChecking channel: #{channel.name}")
        await delete_own_messages(channel, **kwargs)
    print(f"\nTotal deleted in {guild.name}: {total_deleted}")

def build_server_table(guilds):
    table = Table(title="Your Servers", show_header=True, header_style="bold magenta")
    table.add_column("Index", justify="right")
    table.add_column("Server", justify="left")
    table.add_column("ID", justify="right")
    for i, g in enumerate(guilds):
        table.add_row(str(i + 1), g.name, str(g.id))
    return table

def build_channel_table(channels, server_name=""):
    table = Table(title=f"Channels in {server_name}", show_header=True, header_style="bold magenta")
    table.add_column("Index", justify="right")
    table.add_column("Channel", justify="left")
    table.add_column("Type", justify="center")
    for i, c in enumerate(channels):
        ctype = getattr(c, "type", "text")
        table.add_row(str(i + 1), c.name, str(ctype))
    return table

@client.event
async def on_ready():
    console.print(ASCII_HEADER)
    console.print(Panel(f"[bold green]Logged in as {client.user} (ID: {client.user.id})[/bold green]"))
    # Server selection
    server_table = build_server_table(client.guilds)
    console.print(server_table)
    while True:
        guild_idx = console.input("[bold cyan]\nEnter server number: [/bold cyan]")
        if guild_idx.isdigit() and 1 <= int(guild_idx) <= len(client.guilds):
            guild = client.guilds[int(guild_idx) - 1]
            break
        else:
            console.print("[red]Invalid server number. Try again.[/red]")
    # Channel selection
    channel_table = build_channel_table(guild.text_channels, guild.name)
    console.print(channel_table)
    while True:
        chan_idx = console.input("[bold cyan]Enter channel number: [/bold cyan]")
        if chan_idx.isdigit() and 1 <= int(chan_idx) <= len(guild.text_channels):
            channel = guild.text_channels[int(chan_idx) - 1]
            break
        else:
            console.print("[red]Invalid channel number. Try again.[/red]")
    # Prompt for options
    after_str = console.input("[bold yellow]\nDelete messages after date (YYYY-MM-DD, blank for none): [/bold yellow]")
    before_str = console.input("[bold yellow]Delete messages before date (YYYY-MM-DD, blank for none): [/bold yellow]")
    keyword = console.input("[bold yellow]Only delete messages containing keyword (blank for none): [/bold yellow]")
    skip_pinned = console.input("[bold yellow]Skip pinned messages? (Y/n): [/bold yellow]").lower() != "n"
    export_file_raw = console.input("[bold yellow]Export deleted messages to file (filename or blank for none): [/bold yellow]")
    export_file = export_file_raw.strip() if export_file_raw else None
    after = parse_date(after_str) if after_str else None
    before = parse_date(before_str) if before_str else None
    raw_num = console.input("[bold yellow]How many of your last messages to delete? (leave blank for all): [/bold yellow]").strip()
    if raw_num == "" or raw_num is None:
        num = None
    else:
        try:
            num = int(raw_num)
        except ValueError:
            console.print("[red]Invalid number, deleting all messages.[/red]")
            num = None
    keyword_display = keyword if keyword else 'None'
    print()
    console.print(Panel(f"About to delete up to {num if num is not None else 'all'} messages from [bold]{channel.name}[/bold] with filters:\n"
                       f"After: {after}, Before: {before}, Keyword: {keyword_display}, Skip pinned: {skip_pinned}, Export: {export_file or 'None'}", title="\n[bold magenta]Confirm Deletion[/bold magenta]"))
    confirm = console.input("\n[bold red]Proceed? (Y/N): [/bold red]").lower() == "y"
    if confirm:
        await delete_own_messages(
            channel,
            limit=num,
            dry_run=False,
            after=after,
            before=before,
            keyword=keyword,
            skip_pinned=skip_pinned,
            export_file=export_file if export_file else None
        )
    else:
        console.print("[yellow]Cancelled.[/yellow]")
    await client.close()

client.run(TOKEN)
