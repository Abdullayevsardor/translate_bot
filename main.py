import asyncio
import logging
import config
from aiogram import Bot 
from aiogram import Dispatcher
from aiogram import types 
from aiogram.filters import CommandStart, Command

 
 
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

 

@dp.message(CommandStart())
async def handle_start(message:types.Message):
    await message.answer(text = f"Hello, {message.from_user.full_name} !\nYou can send book and choose any language !!!\nI translate for you")

@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "I'm and echo bot.\nSend me anymessage !"
    await message.answer(text= text) 

@dp.message()
async def echo_message(message: types.Message):
    await bot.send_message(
        chat_id = message.chat.id,
        text = "Start processing ...."
    )

 
    await message.answer(
       text = "Wait a second ...",
    )

    if message.document:
        await message.reply("Bu fayl (document).")
    else:
        
        try:
            # await asyncio.sleep(3)
            await message.send_copy(chat_id = message.chat.id)
        except TypeError:
            await message.reply(text='yangilik 😔')
 

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token =config.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())