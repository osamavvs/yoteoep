from pyrogram import filters

links_locked = {}

def register(bot):
    @bot.on_message(filters.text)
    async def check_links(client, message):
        if links_locked.get(message.chat.id) and "http" in message.text:
            await message.delete()
