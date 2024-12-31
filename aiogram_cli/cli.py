import sys
import os

# Your existing templates
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
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token="Bot token")
    dp = Dispatcher(bot)
    await dp.start_polling()


if __name__ == "__main__":
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

def main():
    cmd = sys.argv
    if cmd[1] == "init" and len(cmd) == 3:
        if not os.path.exists(cmd[2]):
            os.mkdir(cmd[2])
        with open(f"{cmd[2]}/bot.py", "w") as f:
            f.write(aiogram_no_template)
        with open(f"{cmd[2]}/requirements.txt", "w") as f:
            f.write("aiogram")
    elif cmd[1] == ("-h" or "--help"):
        print("""Usage:
aiogram:
      init <path> : required   initialize the project
      --with-template: optional    initialize the project with template
""")
    elif cmd[1] == "init" and len(cmd) == 4 and cmd[3] == "--with-template":
        if not os.path.exists(cmd[2]):
            os.mkdir(cmd[2])
        with open(f"{cmd[2]}/bot.py", "w") as f:
            f.write(aiogram_no_template)
        with open(f"{cmd[2]}/requirements.txt", "w") as f:
            f.write("aiogram\nenvirons")
        with open(f"{cmd[2]}/data.py", 'w') as f:
            f.write(environs)
        os.makedirs(f"{cmd[2]}/handlers", mode=777, exist_ok=True)
        with open(f"{cmd[2]}/handlers/__init__.py", "w") as f:
            f.write(handerls_init)
        os.makedirs(f"{cmd[2]}/handlers/users", mode=777, exist_ok=True)
        with open(f"{cmd[2]}/handlers/users/__init__.py", "w") as f:
            f.write(users_init)
        with open(f"{cmd[2]}/handlers/users/start.py", "w") as f:
            f.write(users_start)
        with open(f"{cmd[2]}/handlers/users/help.py", "w") as f:
            f.write(users_help)
        with open(f"{cmd[2]}/handlers/users/echo.py", "w") as f:
            f.write(users_echo)
        os.makedirs(f"{cmd[2]}/handlers/channels", mode=777, exist_ok=True)
        os.makedirs(f"{cmd[2]}/handlers/groups", mode=777, exist_ok=True)
        os.makedirs(f"{cmd[2]}/handlers/groups", mode=777, exist_ok=True)
        with open(f"{cmd[2]}/handlers/groups/__init__.py", "w") as f:
            f.write(groups_init)
        with open(f"{cmd[2]}/handlers/groups/messages.py", "w") as f:
            f.write(groups_messages)
        os.makedirs(f"{cmd[2]}/handlers/channels", mode=777, exist_ok=True)
        with open(f"{cmd[2]}/handlers/channels/__init__.py", "w") as f:
            f.write(channels_init)
        with open(f"{cmd[2]}/handlers/channels/posts.py", "w") as f:
            f.write(channels_posts)
        with open(f"{cmd[2]}/.gitignore", 'w') as f:
            f.write(".env")
        with open(f"{cmd[2]}/.env", 'w') as f:
            f.write("""BOT_TOKEN=telegram_bot_token""")
        with open(f"{cmd[2]}/utils.py", "w") as f:
            f.write(utils)
        os.makedirs(f"{cmd[2]}/keyboards", mode=777, exist_ok=True)
        with open(f"{cmd[2]}/keyboards/__init__.py", "w") as f:
            f.write("from .keyboards import get_keyboard\nfrom .inlinekeyboards import get_inline_keyboard")
        with open(f"{cmd[2]}/keyboards/keyboards.py", "w") as f:
            f.write(keyboards)
        with open(f"{cmd[2]}/keyboards/inlinekeyboards.py", "w") as f:
            f.write(inline_keyboards)
        os.makedirs(f"{cmd[2]}/states", mode=777, exist_ok=True)
        with open(f"{cmd[2]}/states/__init__.py", "w") as f:
            f.write("")
    else:
        print("Error command")
        print("""Usage:
aiogram:
      init <path> : required   initialize the project
      --with-template: optional    initialize the project with template
""")

if __name__ == "__main__":
    main()
