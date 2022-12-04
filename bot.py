# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ContentType, Message


bot = Bot(token='5331287660:AAEc1XKveaIxM_1l1UeaQtkAGS6ItEpLZTY')   # ВВЕДИ СЮДА ТОКЕН БОТА
dp = Dispatcher(bot, storage=MemoryStorage())

class Form(StatesGroup):
    msg = State()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Отправьте сылку на коллекцию")
    await Form.msg.set()

@dp.message_handler(state=Form.msg)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        link = message.text
        print(link)
        await message.answer('На')


if __name__ == '__main__':
    executor.start_polling(dp)