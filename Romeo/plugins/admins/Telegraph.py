import os, asyncio
from typing import Optional
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from telegraph import upload_file
from Romeo import app


@app.on_message(filters.command('tgm'))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("🌹ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...ʙʏ ᴀᴀʀᴏʜɪ ᴍᴜsɪᴄ🌹")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph"

        i.edit(f'🇾ᴏᴜʀ🇹ᴇʟᴇɢʀᴀᴘʜ 👉 {Link}')
