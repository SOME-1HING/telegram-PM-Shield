from pyrogram import filters
from PmBlocker import ubot


@ubot.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmMsg(_, message):
    return await ubot.send_message(
        message.chat.id,
        "Sup",
    )
