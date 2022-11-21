from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ChatType
from PmBlocker import ubot
from PmBlocker.config import USER_ID
from PmBlocker.db import approved_db


@ubot.on_message(filters.all & filters.private & ~filters.me & ~filters.bot)
async def pmblock(_, message: Message):
    user = message.from_user
    if user.is_contact:
        return await approved_db.add_approved_user(user.id)
    if await approved_db.is_user_approved(user.id):
        return
    try:
        await ubot.block_user(user.id)
        await approved_db.remove_approved_user(user.id)
        return await message.reply_text(
            f"`{user.id}` is blocked. Please write your reason to contact to admins of @tyranteyeeee. If the reason is valid, you will be unblocked."
        )
    except Exception as e:
        return await ubot.send_message(USER_ID, f"Error: {e}")


@ubot.on_message(filters.command("block"))
async def block(_, message: Message):
    if message.from_user.id == USER_ID:
        if message.from_user.is_contact:
            return await message.reply_text(
                "User is in contact list, remove them from contact before trying."
            )
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
        return await message.reply_text(f"`{user_id}` is blocked.")
    except Exception as e:
        return await ubot.send_message(USER_ID, f"Error: {e}")
