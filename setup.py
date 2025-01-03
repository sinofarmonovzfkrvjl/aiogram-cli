from setuptools import setup, find_packages

setup(
    name="aiogram-cli",
    version="1.0.6",
    packages=find_packages(),
    install_requires=[
        "hupper"
    ],
    url="https://github.com/sinofarmonovzfkrvjl",
    author="https://t.me/python_dev323",
    description="bu aiogram kutubxonasi uchun aiogram cli (command line tool)",
    entry_points={
        'console_scripts': [
            'aiogram-cli = aiogram_cli.cli:main',
        ],
    },
)
