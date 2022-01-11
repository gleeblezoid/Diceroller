from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gleeblezoid-diceroller",
    description="A dice rolling terminal app made for RPGs",
    version="1.0",
    packages=find_packages(),  # list of all packages
    python_requires=">=3.6",  # any python greater than 2.7
    author="Urse Searle",
    keyword="dice, rpg, gaming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD",
    url="https://github.com/gleeblezoid/Diceroller",
    author_email="hello@gleeblezoid.com",
)
