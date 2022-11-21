from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ChatType
from PmBlocker import ubot
from PmBlocker.config import USER_ID
from PmBlocker.db import approved_db


@ubot.on_message(filters.private & ~filters.me & ~filters.bot)
async def pmblock(_, message: Message):
    user_id = message.from_user.id
    if approved_db.is_user_approved(user_id):
        return
    try:
        await ubot.block_user(user_id)
        await approved_db.remove_approved_user(user_id)
        return await message.reply_text(f"Done, `{user_id}` is blocked.")
    except Exception as e:
        return await ubot.send_message(USER_ID, f"Error: {e}")


@ubot.on_message(filters.command("block"))
async def block(_, message: Message):
    if message.from_user.id == USER_ID:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        elif message.chat.type == ChatType.PRIVATE:
            user_id = message.chat.id
        else:
            if len(message.command) < 2:
                return await message.reply_text("Please mention user id to approve.")
            user_id = int(message.text.split(None, 1)[1])

    try:
        await ubot.block_user(user_id)
        await approved_db.remove_approved_user(user_id)
        return await message.reply_text(f"Done, `{user_id}` is blocked.")
    except Exception as e:
        return await ubot.send_message(USER_ID, f"Error: {e}")
