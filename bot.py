from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, BOT_USERNAME

# Initialize the Pyrogram client
app = Client(
    BOT_USERNAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# /start command
@app.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    await message.reply_text(
        "**👋 Hello!**\n\nSend me a Telegram video or document and I’ll give you the direct download link instantly."
    )

# Handle video or document
@app.on_message(filters.private & (filters.video | filters.document))
async def direct_link_generator(client: Client, message: Message):
    file = message.video or message.document
    file_path = await file.get_file()
    tg_direct_link = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path.file_path}"
    
    await message.reply_text(
        f"✅ **Direct Download Link:**\n\n📥 `{tg_direct_link}`\n\n⚠️ *Keep your bot alive or hosted so the link stays active.*"
    )

# Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    app.run()
