from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, BOT_USERNAME
import logging

logging.basicConfig(level=logging.INFO)

# Initialize the Pyrogram Client
app = Client("VJ_File_Store", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Handle incoming video or document messages
@app.on_message(filters.video | filters.document)
async def direct_link_generator(client, message):
    media = message.video or message.document
    file_id = media.file_id
    file_name = media.file_name or "Telegram_File"

    # Construct streamable link
    stream_url = f"https://t.me/{BOT_USERNAME}?start=watch_{file_id}"

    await message.reply_text(
        f"📂 **File Name:** `{file_name}`\n\n🔗 **Stream Link:** [Click Here]({stream_url})",
        disable_web_page_preview=True
    )

# Handle /start command and deliver file if start param is present
@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    args = message.text.split(None, 1)

    if len(args) == 2 and args[1].startswith("watch_"):
        file_id = args[1].split("_", 1)[1]
        try:
            await client.send_cached_media(chat_id=message.chat.id, media=file_id)
        except Exception as e:
            await message.reply_text(f"❌ Failed to send file.\n\n**Error:** `{e}`")
    else:
        await message.reply_text(
            "👋 **Welcome!**\n\nJust send me a Telegram video or document, and I'll give you a streaming link!"
        )

# Run the bot
app.run()


# --- This keeps the instance alive on platforms like Koyeb ---
from flask import Flask
from threading import Thread

web = Flask('')

@web.route('/')
def home():
    return "Bot is alive!"

def run():
    web.run(host='0.0.0.0', port=8080)

Thread(target=run).start()
# -------------------------------------------------------------

app.run()
