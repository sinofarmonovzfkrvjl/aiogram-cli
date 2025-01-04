import asyncio
import importlib
import sys
import os
from hupper import start_reloader
from colorama import Fore

aiogram_no_template = """from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio
import logging
from data import TOKEN

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.first_name}!")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
"""

handers_init = """from .users import user_router
from .groups import group_router
from .channels import channel_router

def register_all_handlers(router):
    router.include_router(user_router)
    router.include_router(group_router)
    router.include_router(channel_router)
"""

users_init_with_admin = """from .admin import admin_router
from .start import start_router
from .help import help_router
from .echo import echo_router

user_router = admin_router
user_router.include_routers(start_router,help_router, echo_router)
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

users_echo = """from aiogram import Router, F
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

TOKEN = env.str("BOT_TOKEN")
"""

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
aiogram-cli v1.0.8

Usage:
  aiogram-cli init <folder_name>                  Initialize a bot project
  aiogram-cli init <folder_name> --with-template  Initialize a bot project with template files
  aiogram-cli run <bot_file.py>                   Run the specified bot file
  aiogram-cli add admin-handler                   Add admin handler
  aiogram-cli add force-follow-to-channel-handler Add Majburiy Obuna handler
  aiogram-cli add phone-number-handler            Add a handler which handles phone number
  aiogram-cli add location-handler                Add a handler which handles location
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

admin_handler = """from aiogram import Router, F
from aiogram.types import Message
from data import ADMIN_ID

admin_router = Router()

@admin_router.message(F.chat.id == ADMIN_ID)
async def admin_handler(message: Message):
    await message.answer("Salom Admin")
"""

aiogram_with_template = """import asyncio
from aiogram import Dispatcher
from utils import bot, storage, router, set_commands
from handlers import register_all_handlers
import logging

async def main():
    dp = Dispatcher(storage=storage)

    dp.include_router(router)

    register_all_handlers(router)

    await set_commands(bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
"""

phone_number_handler = """

@echo_router.message(F.contact)
async def receive_contact(message: Message):
    phone_number = message.contact.phone_number
    await message.answer(f"phone number: {phone_number}")"""

location_handler = """

@echo_router.message(F.location)
async def receive_location(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    await message.answer(f"latitude: {latitude}, longitude: {longitude}")"""


def main():
    cmd = sys.argv[1:]
    folder = cmd[1]
    if len(cmd) == 0:
        print(usage)
        return

    if cmd[0] == "init" and len(cmd) == 2:
        folder = cmd[1]
        if not os.path.exists(folder):
            os.mkdir(folder)
        with open(f"{folder}/main.py", "w") as f:
            f.write(aiogram_no_template)
        with open(f"{folder}/requirements.txt", "w") as f:
            f.write("aiogram")
        print(Fore.GREEN + "Your Project is successfully created!" + Fore.RESET)
    elif len(cmd) == 3 and cmd[0] == "init" and cmd[2] == "--with-template":
        if not os.path.exists(folder):
            os.mkdir(folder)

        with open(f"{folder}/main.py", "w") as f:
            f.write(aiogram_with_template)
        with open(f"{folder}/requirements.txt", "w") as f:
            f.write("aiogram\nenvirons")
        with open(f"{folder}/data.py", 'w') as f:
            f.write(environs)
        os.makedirs(f"{folder}/handlers", mode=0o777, exist_ok=True)
        with open(f"{folder}/handlers/__init__.py", "w") as f:
            f.write(handers_init)

        os.makedirs(f"{folder}/handlers/users", mode=0o777, exist_ok=True)
        with open(f"{folder}/handlers/users/start.py", "w") as f:
            f.write(users_start)
        with open(f"{folder}/handlers/users/help.py", "w") as f:
            f.write(users_help)
        with open(f"{folder}/handlers/users/echo.py", "w") as f:
            f.write(users_echo)
        with open(f"{cmd[1]}/handlers/users/__init__.py", "w") as f:
            f.write(users_init)

        os.makedirs(f"{folder}/handlers/channels", mode=0o777, exist_ok=True)
        os.makedirs(f"{folder}/handlers/groups", mode=0o777, exist_ok=True)
        with open(f"{folder}/handlers/groups/messages.py", "w") as f:
            f.write(groups_messages)
        with open(f"{cmd[1]}/handlers/groups/__init__.py", "w") as f:
            f.write(groups_init)
        with open(f"{folder}/handlers/channels/posts.py", "w") as f:
            f.write(channels_posts)
        with open(f"{cmd[1]}/handlers/channels/__init__.py", "w") as f:
            f.write(channels_init)

        with open(f"{folder}/.gitignore", 'w') as f:
            f.write(".env")
        with open(f"{folder}/.env", 'w') as f:
            f.write("BOT_TOKEN=your_bot_token_here")
        with open(f"{folder}/utils.py", "w") as f:
            f.write(utils)

        os.makedirs(f"{folder}/keyboards", mode=0o777, exist_ok=True)
        with open(f"{folder}/keyboards/__init__.py", "w") as f:
            f.write("from .keyboards import get_keyboard\nfrom .inlinekeyboards import get_inline_keyboard")
        with open(f"{folder}/keyboards/keyboards.py", "w") as f:
            f.write(keyboards)
        with open(f"{folder}/keyboards/inlinekeyboards.py", "w") as f:
            f.write(inline_keyboards)

        os.makedirs(f"{folder}/states", mode=0o777, exist_ok=True)
        os.makedirs(f"{folder}/middleware", mode=0o777, exist_ok=True)

        with open(f"{folder}/middleware/__init__.py", "w") as f:
            f.write("")

        with open(f"{folder}/states/__init__.py", "w") as f:
            f.write("")

        print(Fore.GREEN + "Your Project is successfully created!" + Fore.RESET)

    elif cmd[0] == "run":
        if len(cmd) == 2:
            import os
            os.system(f"watchmedo auto-restart --patterns=\"*.py\" --recursive -- python {cmd[1]}")
        else:
            print("Usage: aiogram-cli run <bot_file.py>")

    elif cmd[0] == "add":
        if len(cmd) == 3:
            if cmd[1] == "force-follow-to-channel":
                try:
                    with open(f"{cmd[2]}/handlers/users/start.py", "w") as f:
                        f.write(force_follow_to_channel_start_handler)
                    print(Fore.GREEN + "Majburiy obua successfully added" + Fore.RESET)
                except:
                    print(Fore.RED + "XATOLIK: papka topilmadi, papka nomini to'g'ri yozganligizga ishon hosil qiling" + Fore.RESET)
            elif cmd[1] == "admin-handler":
                try:
                    with open(f"{cmd[2]}/handlers/users/admin.py", "w") as f:
                        f.write(admin_handler)
                    with open(f"{cmd[2]}/handlers/users/__init__.py", "w") as f:
                        f.write(users_init_with_admin)
                    with open(f"{cmd[2]}/.env", "a") as f:
                        f.write("\nADMIN_ID=your_admin_id_here")
                    with open(f"{cmd[2]}/data.py", "a") as f:
                        f.write("""\nADMIN_ID = env.int("ADMIN_ID")""")
                    print(Fore.GREEN + "Admin Handler muvaffaqiyatli qo'shildi" + Fore.RESET)
                except:
                    print(Fore.RED + "XATOLIK: papka topilmadi, papka nomini to'g'ri yozganligizga ishon hosil qiling" + Fore.RESET)
            elif cmd[1] == "phone-number-handler":
                with open(f"{cmd[2]}/handlers/users/echo.py", "a") as f:
                    f.write(phone_number_handler)
            elif cmd[1] == "location-handler":
                with open(f"{cmd[2]}/handlers/users/echo.py", "a") as f:
                    f.write(location_handler)
            else:
                print(Fore.RED + f"ERROR: {cmd[1]} nomli handler mavjud emas" + Fore.RESET)
        elif len(cmd) == 2:
            print(Fore.RED + "ERROR: papka nomini yozishni unitdingiz\n" + Fore.RESET + f"aiogram-cli.exe add {cmd[1]} <papka-nomi>")

    elif cmd[0] == "remove":
        if len(cmd) == 3:
            if cmd[1] == "force-follow-to-channel":
                try:
                    with open(f"{cmd[2]}/handlers/users/start.py", "w") as f:
                        f.write(users_start)
                except:
                    print(Fore.RED + "XATOLIK: papka topilmadi, papka nomini to'g'ri yozganligizga ishon hosil qiling" + Fore.RESET)
        elif len(cmd) == 2:
            print(Fore.RED + "ERROR: papka nomini yozishni unitdingiz\n" + Fore.RESET + f"aiogram-cli.exe remove {cmd[1]} <papka-nomi>")

    elif cmd[0] in ("-h", "--help"):
        print(usage)
    else:
        print(f"Error: Nomalum komanda '{cmd[0]}'")
        print(usage)


if __name__ == "__main__":
    main()