import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import *
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import img_btn

API_TOKEN = '5946381857:AAGPXyRJtN9c-N4YVRvgpwzMFDTngG8ZyH8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage
dp = Dispatcher(bot=bot, storage=storage)

images = ['minecraft.jpg','roblox1234567890','stick war`.wepb']

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['img'])
async def send_welcome(message: Message, state: FSMContext):
    btn = await img_btn(1, len(images))
    await state.update_data(page=1)
    await message.answer_photo(InputFile('minecraft.jpg'),reply_markup=btn)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)