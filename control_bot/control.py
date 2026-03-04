from telethon import TelegramClient, events
from config import BOT_TOKEN, ADMIN_ID, MAIN_PATH
import os, subprocess

# البوت
client = TelegramClient('control_bot', api_id=0, api_hash='dummy').start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(from_users=ADMIN_ID))
async def handler(event):
    text = event.raw_text.lower()

    if "تشغيل" in text:
        os.system(f"cd {MAIN_PATH} && nohup python3 main.py &")
        await event.reply("✅ تم تشغيل السورس")

    elif "ايقاف" in text:
        os.system("pkill -f main.py")
        await event.reply("🛑 تم ايقاف السورس")

    elif "تحديث" in text:
        os.system(f"cd {MAIN_PATH} && git pull")
        os.system("pkill -f main.py")
        os.system(f"cd {MAIN_PATH} && nohup python3 main.py &")
        await event.reply("🔄 تم التحديث واعادة التشغيل")

    elif "حالة" in text:
        result = subprocess.getoutput("pgrep -f main.py")
        if result:
            await event.reply("🟢 السورس يعمل")
        else:
            await event.reply("🔴 السورس متوقف")

print("🔥 بوت التحكم شغال الآن!")
client.run_until_disconnected()
