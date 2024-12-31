from setuptools import setup, find_packages

setup(
    name="aiogram-cli",
    version="2.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'aiogram-cli = aiogram_cli.cli:main',
        ],
    },
)
