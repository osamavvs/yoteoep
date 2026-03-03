from aiogram import types

def register_handlers(dp):
    @dp.callback_query_handler(lambda c: c.data == 'ranks')
    async def show_ranks(callback_query: types.CallbackQuery):
        await callback_query.message.answer("""
👑 الرتب:

• مطور
• مالك
• ادمن
• عضو
""")
