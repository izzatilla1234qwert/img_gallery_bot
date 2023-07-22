

import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.types import *

from keyboards import *
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5946381857:AAHy9nMe0Ta3QPTLPuPgsiCtssT7l8Nizwo'

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

images = ["roblox1234567890.png","stick war.webp","minecraft.jpg"]

img_id = 0

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply('salom')

@dp.message_handler(commands='img')
async def send_image(message: types.Message):
    global img_id
    btn = await img_btn(img_id+1, len(images))
    await message.answer_photo(types.InputFile(images[img_id]), reply_markup=btn)


@dp.callback_query_handler(text = 'next')
async def oldinga(call :types.CallbackQuery):
    global img_id
    img_id+=1
    btn = await img_btn(img_id+1, len(images))
    await call.message.answer_photo(types.InputFile(images[img_id]), reply_markup=btn)
        
    
@dp.callback_query_handler(text = 'prev')
async def oldinga(call :types.CallbackQuery):
    global img_id
    img_id-=1
    # await call.message.answer(img_id)
    btn = await img_btn(img_id+1, len(images))
    await call.message.answer_photo(types.InputFile(images[img_id]), reply_markup=btn)


if __name__ == '__main__':
    executor.start_polling(dp)