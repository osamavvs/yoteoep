from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN
from handlers import menu, protect, ranks  # استيراد handlers

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# تسجيل handlers
menu.register_handlers(dp)
protect.register_handlers(dp)
ranks.register_handlers(dp)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply("""
༺ No Doubt Protection ༻

🛡 بوت حماية احترافي
استخدم /menu لعرض الاعدادات
""")

if __name__ == "__main__":
    print("Bot Started ✅")
    executor.start_polling(dp, skip_updates=True)
