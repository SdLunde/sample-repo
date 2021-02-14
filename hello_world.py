import sys
import math
import requests

# print(sys.version)
# print(sys.executable)


def greet(who_to_greet):
    greeting = "hello, {}".format(who_to_greet)
    return greeting


print(greet("world"))
print(greet("Corey"))

# Command pallet ctrl + shift + p


# create virtual environment in terminal by typing python -m venv venv

# Sometimes it throws errors when using pip and installing modules globally not locally in venv
# C:\Users\sindr\OneDrive\Skrivebord\vscode\venv\Scripts\python.exe -m pip install --upgrade pip
# c:/Users/sindr/OneDrive/Skrivebord/vscode/venv/Scripts/python.exe -m pip install requests