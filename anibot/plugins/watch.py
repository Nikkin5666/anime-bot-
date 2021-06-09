import os

from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(filters.command(["start"], prefixes=["!", "/"]))

async def get_watch_order(client: Client, message: Message):

    if message.chat.id == message.from_user.id:

        await client.send_animation(message.chat.id, os.environ.get("GIF_LINK"), "Regards: @DreamOwO", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Contact", url="https://t.me/dreamowo"))]])
