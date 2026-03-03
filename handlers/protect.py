from aiogram import types
import json

def register_handlers(dp):
    @dp.callback_query_handler(lambda c: c.data == 'settings')
    async def protect_settings(callback_query: types.CallbackQuery):
        await callback_query.message.answer("""
🔒 اوامر الحماية:

/قفل الروابط
/فتح الروابط
/قفل الصور
/فتح الصور
""")
