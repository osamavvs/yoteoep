from pyrogram import Client
import config
from plugins import general, admin, protection

bot = Client("MainBot", bot_token=config.TOKEN)

# تسجيل كل الملفات
general.register(bot)
admin.register(bot)
protection.register(bot)

print("🔥 البوت الأساسي بدأ العمل الآن!")
bot.run()
