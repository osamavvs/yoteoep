from pyrogram import filters

def register(bot):
    @bot.on_message(filters.text)
    async def general_commands(client, message):
        if message.text == "ابدأ":
            await message.reply("🌙 مرحبا بك في بوت الحماية الاحترافي!")

        elif message.text == "مساعدة":
            await message.reply("""
📌 أوامر البوت:

- كتم / الغاء كتم
- حظر / الغاء حظر
- قفل روابط / فتح روابط
- عرض الحالة
            """)
