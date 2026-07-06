import os
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "tele_compress",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "Hola, soy Tele Compress.\n\n"
        "Bot iniciado correctamente."
    )


print("Bot iniciado...")

app.run()