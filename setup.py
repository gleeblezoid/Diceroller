from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gleeblezoid-diceroller",
    description="A dice rolling terminal app made for RPGs",
    version="1.0",
    packages=[
        "gleeblezoid_diceroller",
        "gleeblezoid_diceroller.lib",
        "gleeblezoid_diceroller.lib.menus",
        "gleeblezoid_diceroller.lib.rollers",
        "gleeblezoid_diceroller.lib.RPG_systems",
    ],
    entry_points={
        "console_scripts": [
            "gleeblezoid_diceroller = gleeblezoid_diceroller.diceroller:main"
        ]
    },
    python_requires=">=3.6",  # any python greater than 2.7
    author="Urse Searle",
    keyword="dice, rpg, gaming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD",
    url="https://github.com/gleeblezoid/Diceroller",
    author_email="hello@gleeblezoid.com",
)
