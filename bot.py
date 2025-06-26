# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import re
import os
from os import environ
from pyrogram import Client, filters
from Script import script

# Regex to validate admin IDs
id_pattern = re.compile(r'^.\d+$')

# Enable/Disable helper
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot Information
API_ID = int(environ.get("API_ID", "25399581"))
API_HASH = environ.get("API_HASH", "78e8a7d45e41484937c47acfdf1f6433")
BOT_TOKEN = environ.get("BOT_TOKEN", "7710449342:AAGI3eFX7ahHb93BimGOLp76SJsoHVQj31U")
BOT_USERNAME = environ.get("BOT_USERNAME", "Bnthmzhadwnbot")  # without @

# Bot Start Picture
PICS = (environ.get('PICS', 'https://graph.org/file/ce1723991756e48c35aa1.jpg')).split()

# Admins
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6322672707').split()]

# Port
PORT = environ.get("PORT", "8080")

# Clone Info
CLONE_MODE = is_enabled(environ.get('CLONE_MODE', "False"), False)
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://mohommediflaan:Zf0R9eAKTgs8jb6W@cluster0.hhpr2lx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CDB_NAME = environ.get("CDB_NAME", "clonetechvj")

# Database Info
DB_URI = environ.get("DB_URI", "mongodb+srv://mohommediflaan:Zf0R9eAKTgs8jb6W@cluster0.hhpr2lx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "mohommediflan")

# Auto Delete Info
AUTO_DELETE_MODE = is_enabled(environ.get('AUTO_DELETE_MODE', "False"), False)
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30"))
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800"))

# Channel Info
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002768282561"))

# Caption
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable / Disable
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

# Verify Info
VERIFY_MODE = is_enabled(environ.get('VERIFY_MODE', "False"), False)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "")
SHORTLINK_API = environ.get("SHORTLINK_API", "")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "")

# Website Info
WEBSITE_URL_MODE = is_enabled(environ.get('WEBSITE_URL_MODE', "False"), False)
WEBSITE_URL = environ.get("WEBSITE_URL", "https://tamilben.blogspot.com/2025/06/bot.html")

# File Stream Config
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', "True"), True)
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
ON_HEROKU = 'DYNO' in environ
URL = environ.get("URL", "https://tamilben.blogspot.com/2025/06/bot.html")

# Pyrogram Client
app = Client("VJ_File_Store", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.video | filters.document)
async def direct_link_generator(client, message):
    media = message.video or message.document
    file_id = media.file_id
    file_name = media.file_name or "File"
    
    stream_url = f"https://t.me/{BOT_USERNAME}?start=watch_{file_id}"

    await message.reply_text(
        f"\n📂 **File Name:** `{file_name}`\n\n🔗 **Stream Link:** [Click Here]({stream_url})",
        disable_web_page_preview=True
    )


@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    args = message.text.split(None, 1)
    if len(args) == 2 and args[1].startswith("watch_"):
        file_id = args[1].split("_", 1)[1]
        try:
            await client.send_cached_media(chat_id=message.chat.id, media=file_id)
        except Exception as e:
            await message.reply_text(f"❌ Failed to send file.\nError: {e}")
    else:
        await message.reply_text("👋 Welcome! Send me a video or document to get a streaming link.")


app.run()# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import re
import os
from os import environ
from pyrogram import Client, filters
from Script import script

# Regex to validate admin IDs
id_pattern = re.compile(r'^.\d+$')

# Enable/Disable helper
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot Information
API_ID = int(environ.get("API_ID", "25399581"))
API_HASH = environ.get("API_HASH", "78e8a7d45e41484937c47acfdf1f6433")
BOT_TOKEN = environ.get("BOT_TOKEN", "7710449342:AAGI3eFX7ahHb93BimGOLp76SJsoHVQj31U")
BOT_USERNAME = environ.get("BOT_USERNAME", "Bnthmzhadwnbot")  # without @

# Bot Start Picture
PICS = (environ.get('PICS', 'https://graph.org/file/ce1723991756e48c35aa1.jpg')).split()

# Admins
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6322672707').split()]

# Port
PORT = environ.get("PORT", "8080")

# Clone Info
CLONE_MODE = is_enabled(environ.get('CLONE_MODE', "False"), False)
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://mohommediflaan:Zf0R9eAKTgs8jb6W@cluster0.hhpr2lx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CDB_NAME = environ.get("CDB_NAME", "clonetechvj")

# Database Info
DB_URI = environ.get("DB_URI", "mongodb+srv://mohommediflaan:Zf0R9eAKTgs8jb6W@cluster0.hhpr2lx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "mohommediflan")

# Auto Delete Info
AUTO_DELETE_MODE = is_enabled(environ.get('AUTO_DELETE_MODE', "False"), False)
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30"))
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800"))

# Channel Info
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002768282561"))

# Caption
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable / Disable
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

# Verify Info
VERIFY_MODE = is_enabled(environ.get('VERIFY_MODE', "False"), False)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "")
SHORTLINK_API = environ.get("SHORTLINK_API", "")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "")

# Website Info
WEBSITE_URL_MODE = is_enabled(environ.get('WEBSITE_URL_MODE', "False"), False)
WEBSITE_URL = environ.get("WEBSITE_URL", "https://tamilben.blogspot.com/2025/06/bot.html")

# File Stream Config
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', "True"), True)
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
ON_HEROKU = 'DYNO' in environ
URL = environ.get("URL", "https://tamilben.blogspot.com/2025/06/bot.html")

# Pyrogram Client
app = Client("VJ_File_Store", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.video | filters.document)
async def direct_link_generator(client, message):
    media = message.video or message.document
    file_id = media.file_id
    file_name = media.file_name or "File"
    
    stream_url = f"https://t.me/{BOT_USERNAME}?start=watch_{file_id}"

    await message.reply_text(
        f"\n📂 **File Name:** `{file_name}`\n\n🔗 **Stream Link:** [Click Here]({stream_url})",
        disable_web_page_preview=True
    )


@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    args = message.text.split(None, 1)
    if len(args) == 2 and args[1].startswith("watch_"):
        file_id = args[1].split("_", 1)[1]
        try:
            await client.send_cached_media(chat_id=message.chat.id, media=file_id)
        except Exception as e:
            await message.reply_text(f"❌ Failed to send file.\nError: {e}")
    else:
        await message.reply_text("👋 Welcome! Send me a video or document to get a streaming link.")


app.run()
