from pyrogram import filters
from pyrogram.types import Message
from PmBlocker import ubot
from PmBlocker.db import approved_db


@ubot.on_message(filters.private & ~filters.me & ~filters.bot)
async def block(_, message: Message):
    user_id = message.from_user.id
    if approved_db.is_user_approved(user_id):
        return
    try:
        await ubot.block_user(user_id)
        await approved_db.remove_approved_user(user_id)
        return await message.reply_text(f"Done, `{user_id}` is blocked.")
    except Exception as e:
        return await message.reply_text(f"Error: {e}")
