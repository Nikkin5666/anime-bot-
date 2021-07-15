import os

from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(filters.command(["start"], prefixes=["!", "/"]))

async def get_watch_order(client: Client, message: Message):

    if message.chat.id == message.from_user.id:

        await client.send_message(1865747807, f"New freaking user started the bot \n\n{message.from_user.mention} \n**ID:**{message.from_user.id}")

        await client.send_animation(message.chat.id, os.environ.get("GIF_LINK"), "I am Imaginary Gf Bot the gf of a sad soul (@Dotdotdot_dot_dot)", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Press", url="t.me/Dotdotdot_dot_dot")]]))
