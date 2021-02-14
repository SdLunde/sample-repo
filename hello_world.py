import requests

def greet(who_to_greet):
    greeting = "hello, {}".format(who_to_greet)
    return greeting

print(greet("Sindre"))

# Command pallet ctrl + shift + p


# create virtual environment in terminal by typing python -m venv venv

# Sometimes it throws errors when using pip and installing modules globally not locally in venv
# C:\Users\sindr\OneDrive\Skrivebord\vscode\venv\Scripts\python.exe -m pip install --upgrade pip
# c:/Users/sindr/OneDrive/Skrivebord/vscode/venv/Scripts/python.exe -m pip install requests
# git config --global user.name "SdLunde"
# git config --global user.email "sindre.djupevik.lunde@gmail.com"
# git config --list
