from setuptools import setup, find_packages

setup(
    name="aiogram-cli",
    version="1.0.4",
    packages=find_packages(),
    install_requires=[
        "hupper"
    ],
    entry_points={
        'console_scripts': [
            'aiogram-cli = aiogram_cli.cli:main',
        ],
    },
)
