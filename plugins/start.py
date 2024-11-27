from pyrogram import Client, filters
from config import LOG_CHANNEL
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)


LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    await db.is_user_exist(m.from_user.id)
    await db.add_user(m.from_user.id, m.from_user.first_name)
    await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    await m.reply_photo(f"https://envs.sh/3eW.jpeg",
        caption="**ʜɪ** 🦋\n\n**ɪ ᴀᴍ ᴀ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ**\n\n⭕ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[ɴɪꜱʜᴀɴᴛ](https://t.me/Nishant_0786)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🦋 JᴏɪN Fᴏʀ Mᴏᴠɪᴇs 🦋', url='https://t.me/Ni_Movie_Request_Group')
                    ],  
                    [
                        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ ❤️‍🔥", url='https://t.me/Nishant_0786'),
                        InlineKeyboardButton("BᴀᴄᴋUᴘ", url='https://t.me/Ni_Movies')
                    ]
                ]
            )
        )
  
