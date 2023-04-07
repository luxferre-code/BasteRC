"""
Don't modify this file !!
"""

from colorama import Fore, Back, Style, init

AUTHOR = "Valentin Thuillier <@luxferre-code>"
VERSION = "0.0.1 - Alpha 1"
LICENSE = "MIT License"

TEXT_FORMAT = {
    "normal": "0",
    "bold": "1",
    "underline": "4",
}

COLORS = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
}

BACKGROUND_COLORS = {
    "black_bg": "40",
    "red_bg": "41",
    "green_bg": "42",
    "yellow_bg": "43",
    "blue_bg": "44",
    "magenta_bg": "45",
    "cyan_bg": "46",
    "white_bg": "47",
}

COLORAMA_PATTERN = {
    "black": Fore.BLACK,
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE,
    "black_bg": Back.BLACK,
    "red_bg": Back.RED,
    "green_bg": Back.GREEN,
    "yellow_bg": Back.YELLOW,
    "blue_bg": Back.BLUE,
    "magenta_bg": Back.MAGENTA,
    "cyan_bg": Back.CYAN,
    "white_bg": Back.WHITE,
    "normal": Style.NORMAL,
    "bold": Style.BRIGHT,
    "underline": Style.DIM,
}