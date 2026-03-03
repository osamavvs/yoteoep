from aiogram import types

def register_handlers(dp):
    @dp.message_handler(commands=['menu'])
    async def menu_cmd(message: types.Message):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("⚙️ اعدادات الحماية", callback_data="settings"))
        keyboard.add(types.InlineKeyboardButton("👮‍♂️ الرتب", callback_data="ranks"))
        await message.reply("اختر من القائمة:", reply_markup=keyboard)
