from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import types

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
	await message.answer("Хай!!!")

@start_router.message(Command('info'))
async def cmd_info(message: Message):
	await message.answer("T bank")


@start_router.message(Command("admin"))
async def cmd_admin(message: Message):
    kb = [
        [types.KeyboardButton(text="Админы")],
        [types.KeyboardButton(text="Добавить Админов")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Выберите опцию", reply_markup=keyboard)
