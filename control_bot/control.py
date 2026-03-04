import os
import subprocess
from pyrogram import Client, filters
from config import BOT_TOKEN, ADMIN_ID, MAIN_PATH
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

app = Client("control_bot", bot_token=BOT_TOKEN)

def is_admin(_, __, message):
    return message.from_user.id == ADMIN_ID

admin_filter = filters.create(is_admin)

panel = InlineKeyboardMarkup([
    [InlineKeyboardButton("▶️ تشغيل السورس", callback_data="start")],
    [InlineKeyboardButton("⏹ ايقاف السورس", callback_data="stop")],
    [InlineKeyboardButton("⬆️ تحديث السورس", callback_data="update")],
    [InlineKeyboardButton("📊 حالة السورس", callback_data="status")]
])

@app.on_message(filters.private & admin_filter)
async def show_panel(client, message):
    await message.reply(
        "👑 مرحباً بك في لوحة تحكم السورس الأساسي",
        reply_markup=panel
    )

@app.on_callback_query()
async def handle_buttons(client: Client, callback: CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        return await callback.answer("❌ غير مصرح", show_alert=True)

    data = callback.data

    if data == "start":
        os.system(f"cd {MAIN_PATH} && nohup python3 main.py &")
        await callback.answer("✅ تم تشغيل السورس")

    elif data == "stop":
        os.system("pkill -f main.py")
        await callback.answer("🛑 تم ايقاف السورس")

    elif data == "update":
        os.system(f"cd {MAIN_PATH} && git pull")
        os.system("pkill -f main.py")
        os.system(f"cd {MAIN_PATH} && nohup python3 main.py &")
        await callback.answer("🔄 تم التحديث واعادة التشغيل")

    elif data == "status":
        result = subprocess.getoutput("pgrep -f main.py")
        if result:
            await callback.answer("🟢 السورس يعمل")
        else:
            await callback.answer("🔴 السورس متوقف")

print("🔥 بوت التحكم شغال الآن!")
app.run()
