aiogram_no_template = """from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio
import logging

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.first_name}!")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    TOKEN = "bot_toknen"
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
"""

handerls_init = """from .users import user_router
from .groups import group_router
from .channels import channel_router

def register_all_handlers(router):
    router.include_router(user_router)
    router.include_router(group_router)
    router.include_router(channel_router)
"""

users_init = """from .start import start_router
from .help import help_router
from .echo import echo_router

user_router = start_router
user_router.include_routers(help_router, echo_router)
"""

users_start = """from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

start_router = Router()

@start_router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f"Salom {message.from_user.full_name}")"""

users_help = """from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

help_router = Router()

@help_router.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Sizga qanday yordam beraolaman?")"""

users_echo = """from aiogram import Router
from aiogram.types import Message

echo_router = Router()

@echo_router.message()
async def echo(message: Message):
    await message.answer(message.text)"""

groups_init = """from .messages import group_message_router

group_router = group_message_router
"""

groups_messages = """from aiogram import Router, F
from aiogram.types import Message

group_message_router = Router()

@group_message_router.message(F.chat.type == "group" or F.chat.type == "supergroup")
async def handle_group_message(message: Message):
    await message.answer("This is a group message handler.")"""

channels_init = """from .posts import channel_post_router

channel_router = channel_post_router"""

channels_posts = """from aiogram import Router, F
from aiogram.types import Message

channel_post_router = Router()

@channel_post_router.message(F.chat.type == "channel")
async def handle_channel_post(message: Message):
    await message.answer("This is a channel post handler.")
"""

environs = """from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("BOT_TOKEN")"""

utils = """from aiogram import Bot
from aiogram.dispatcher.router import Router
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from data import TOKEN

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
router = Router()

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/help", description="Get help"),
    ]
    await bot.set_my_commands(commands)
"""

keyboards = """from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[ 
        [KeyboardButton(text="Hello")],
    ])
    return keyboard"""

inline_keyboards = """from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_inline_keyboard():
    keyboards = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [InlineKeyboardButton(text="Hello", callback_data="hello")],
    ])
    return keyboards"""

usage ='''
aiogram-cli v1.0.5

Usage:
  aiogram-cli init <folder_name>                  Initialize a bot project
  aiogram-cli init <folder_name> --with-template  Initialize a bot project with template files
  aiogram-cli run <bot_file.py>                   Run the specified bot file (ishlamayapti)
  aiogram-cli -h | --help                         Show this message
'''

force_follow_to_channel_start_handler = """from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from utils import Bot

start_router = Router()

CHANNEL_ID = "kanal_id_sini_yozing"

@start_router.message(CommandStart())
async def start_command(message: Message, bot: Bot):
    chat_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if chat_member.status == "left":
        await message.answer("")
    else:
        await message.answer(f"Salom {message.from_user.full_name}")
"""