from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
import config

def is_admin(user_id):
    return user_id in config.ADMINS

# لوحة تحكم Inline
def admin_panel(chat_id):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔇 كتم", callback_data=f"mute_{chat_id}"),
         InlineKeyboardButton("✅ الغاء كتم", callback_data=f"unmute_{chat_id}")],
        [InlineKeyboardButton("🔒 قفل روابط", callback_data=f"lock_links_{chat_id}"),
         InlineKeyboardButton("🔓 فتح روابط", callback_data=f"unlock_links_{chat_id}")],
    ])

def register(bot):
    @bot.on_message(filters.text)
    async def show_panel(client, message):
        if not is_admin(message.from_user.id):
            return
        await message.reply(
            "👑 مرحباً بك في لوحة تحكم البوت",
            reply_markup=admin_panel(message.chat.id)
        )
