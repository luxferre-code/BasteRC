"""
BasteRC - A simple modifyable RC file for bash
Author : Valentin Thuillier <@luxferre-code>
"""

# Documentation utilise: https://www.tecmint.com/customize-bash-colors-terminal-prompt-linux/

from bashrc import BashRC
import os, sys
from cutie import *
from consts import *

if __name__ != "__main__":
    raise Exception("This file is not a module !")

# Init bashrc

username = os.getlogin()
hostname = os.uname().nodename
bashrc = BashRC(username, hostname)

# Selection of user settings

print("Welcome to BasteRC !")
print("This program will help you to create a custom bashrc file.")
print("")
print("First, let's start with the user settings.")

print("What color do you want for your username ?")
user_color = select(
    [
        f"{COLORAMA_PATTERN['black']}Black{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['red']}Red{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['green']}Green{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['yellow']}Yellow{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['blue']}Blue{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['magenta']}Magenta{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['cyan']}Cyan{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['white']}White{COLORAMA_PATTERN['normal']}",
        f"Any{COLORAMA_PATTERN['normal']}"
    ]
)

print("What background color do you want for your username ?")
user_bg = select(
    [
        f"{COLORAMA_PATTERN['black']}Black{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['red']}Red{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['green']}Green{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['yellow']}Yellow{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['blue']}Blue{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['magenta']}Magenta{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['cyan']}Cyan{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['white']}White{COLORAMA_PATTERN['normal']}",
        f"Any{COLORAMA_PATTERN['normal']}"
    ]
)

print("What text format do you want for your username ?")
user_style = select(
    [
        f"{COLORAMA_PATTERN['normal']}Normal{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['bold']}Bold{COLORAMA_PATTERN['normal']}",
        f"{COLORAMA_PATTERN['underline']}Underline{COLORAMA_PATTERN['normal']}",
    ]
)

bashrc.set_user_color({
    "color": list(COLORS.keys())[user_color],
    "bg": list(BACKGROUND_COLORS.keys())[user_bg],
    "style": list(TEXT_FORMAT.keys())[user_style]
})

bashrc.appercu()
