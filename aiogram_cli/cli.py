import asyncio
import importlib
import sys
import os
from hupper import start_reloader
from colorama import Fore
from variables import *

def run_bot_file(bot_file):
    # This function will be used to run the bot file
    asyncio.run(importlib.import_module(bot_file).main())

def main():
    cmd = sys.argv[1:]
    if len(cmd) == 0:
        print(usage)
        return

    if cmd[0] == "init" and len(cmd) == 2:
        folder = cmd[2]
        if not os.path.exists(folder):
            os.mkdir(folder)
        with open(f"{folder}/main.py", "w") as f:
            f.write(aiogram_no_template)
        with open(f"{folder}/requirements.txt", "w") as f:
            f.write("aiogram")
        print(Fore.GREEN + "Your Project is successfully created!" + Fore.RESET)
    elif len(cmd) == 3 and cmd[0] == "init" and cmd[2] == "--with-template":
        folder = cmd[1]
        if not os.path.exists(folder):
            os.mkdir(folder)

        with open(f"{folder}/main.py", "w") as f:
            f.write(aiogram_no_template)
        with open(f"{folder}/requirements.txt", "w") as f:
            f.write("aiogram\nenvirons")
        with open(f"{folder}/data.py", 'w') as f:
            f.write(environs)
        os.makedirs(f"{folder}/handlers", mode=0o777, exist_ok=True)
        with open(f"{folder}/handlers/__init__.py", "w") as f:
            f.write(handerls_init)

        os.makedirs(f"{folder}/handlers/users", mode=0o777, exist_ok=True)
        with open(f"{folder}/handlers/users/start.py", "w") as f:
            f.write(users_start)
        with open(f"{folder}/handlers/users/help.py", "w") as f:
            f.write(users_help)
        with open(f"{folder}/handlers/users/echo.py", "w") as f:
            f.write(users_echo)

        os.makedirs(f"{folder}/handlers/channels", mode=0o777, exist_ok=True)
        os.makedirs(f"{folder}/handlers/groups", mode=0o777, exist_ok=True)
        with open(f"{folder}/handlers/groups/messages.py", "w") as f:
            f.write(groups_messages)
        with open(f"{folder}/handlers/channels/posts.py", "w") as f:
            f.write(channels_posts)

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

        print(Fore.GREEN + "Your Project is successfully created!" + Fore.RESET)

    elif cmd[0] == "run":
        if len(cmd) == 3:
            bot_file = cmd[1]
            reloader = start_reloader(run_bot_file(bot_file))
            asyncio.run(importlib.import_module(bot_file).main())
        else:
            print("Usage: aiogram-cli run <bot_file.py>")

    elif cmd[0] == "add":
        if cmd[1] == "force-follow-to-channel" and len(cmd) == 3:
            try:
                with open(f"{cmd[2]}/handlers/users/start.py", "w") as f:
                    f.write(force_follow_to_channel_start_handler)
            except:
                print(Fore.RED + "XATOLIK: papka topilmadi, papka nomini to'g'ri yozganligizga ishon hosil qiling" + Fore.RESET)
        elif len(cmd) == 2:
            print(Fore.RED + "ERROR: papka nomini yozishni unitdingiz\n" + Fore.RESET + f"aiogram-cli.exe add {cmd[1]} <papka-nomi>")

    elif cmd[0] == "remove":
        if cmd[1] == "force-follow-to-channel" and len(cmd) == 3:
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