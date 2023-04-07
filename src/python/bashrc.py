from consts import *


class BashRC:
    def __init__(self, username: str, hostname: str) -> None:
        init(autoreset=True)
        self.__user_color: str = ""
        self.__user_bg: str = ""
        self.__user_style: str = ""
        self.__host_color: str = ""
        self.__host_bg: str = ""
        self.__host_style: str = ""
        self.__path_color: str = ""
        self.__path_bg: str = ""
        self.__path_style: str = ""
        self.__prompt_color: str = ""
        self.__prompt_bg: str = ""
        self.__prompt_style: str = ""

        self.__alias: dict[str] = {}

        self.__username: str = username
        self.__hostname: str = hostname

    def get_user_color(self) -> str:
        return self.__user_color

    def get_host_color(self) -> str:
        return self.__host_color

    def get_path_color(self) -> str:
        return self.__path_color

    def get_username(self) -> str:
        return self.__username

    def get_hostname(self) -> str:
        return self.__hostname

    def set_user_color(self, color: dict[str]) -> None:
        if "color" in color.keys():
            self.__user_color = color["color"]
        if "bg" in color.keys():
            self.__user_bg = color["bg"]
        if "style" in color.keys():
            self.__user_style = color["style"]

    def set_host_color(self, color: dict[str]) -> None:
        if "color" in color.keys():
            self.__host_color = color["color"]
        if "bg" in color.keys():
            self.__host_bg = color["bg"]
        if "style" in color.keys():
            self.__host_style = color["style"]

    def set_path_color(self, color: dict[str]) -> None:
        if "color" in color.keys():
            self.__path_color = color["color"]
        if "bg" in color.keys():
            self.__path_bg = color["bg"]
        if "style" in color.keys():
            self.__path_style = color["style"]

    def get_representation_user(self) -> str:
        return f"""{COLORAMA_PATTERN[self.get_user_color()]}{COLORAMA_PATTERN[self.get_user_bg()]}{COLORAMA_PATTERN[self.get_user_style()]}{self.get_username()}{COLORAMA_PATTERN['normal']}"""

    def get_representation_host(self) -> str:
        return f"""{COLORAMA_PATTERN[self.get_host_color()]}{COLORAMA_PATTERN[self.get_host_bg()]}{COLORAMA_PATTERN[self.get_host_style()]}{self.get_hostname()}{COLORAMA_PATTERN['normal']}"""

    def get_representation_path(self) -> str:
        return f"""{COLORAMA_PATTERN[self.get_path_color()]}{COLORAMA_PATTERN[self.get_path_bg()]}{COLORAMA_PATTERN[self.get_path_style()]}~{COLORAMA_PATTERN['normal']}"""

    def appercu(self) -> None:
        print(f"{self.get_representation_user()}@{self.get_representation_host()}:{self.get_representation_path()}$ ")

    def get_user_bg(self) -> str:
        return self.__user_bg

    def get_host_bg(self) -> str:
        return self.__host_bg

    def get_path_bg(self) -> str:
        return self.__path_bg

    def get_user_style(self) -> str:
        return self.__user_style

    def get_host_style(self) -> str:
        return self.__host_style

    def get_path_style(self) -> str:
        return self.__path_style

    def get_code_user(self) -> str:
        result: str = "\\e["
        if self.get_user_bg() != "":
            result += f"{BACKGROUND_COLORS[self.get_user_bg()]};"
        if self.get_user_color() != "":
            result += f"{COLORS[self.get_user_color()]};"
        if self.get_user_style() != "":
            result += f"{TEXT_FORMAT[self.get_user_style()]}"

        if result == "\\e[":
            return ""

        return result + "m[\\u"

    def get_code_host(self) -> str:
        result: str = "\\e["
        if self.get_host_bg() != "":
            result += f"{BACKGROUND_COLORS[self.get_host_bg()]};"
        if self.get_host_color() != "":
            result += f"{COLORS[self.get_host_color()]};"
        if self.get_host_style() != "":
            result += f"{TEXT_FORMAT[self.get_host_style()]}"

        if result == "\\e[":
            return ""

        return result + "m\\h"

    def get_code_path(self) -> str:
        result: str = "\\e["
        if self.get_path_bg() != "":
            result += f"{BACKGROUND_COLORS[self.get_path_bg()]};"
        if self.get_path_color() != "":
            result += f"{COLORS[self.get_path_color()]};"
        if self.get_path_style() != "":
            result += f"{TEXT_FORMAT[self.get_path_style()]}"

        if result == "\\e[":
            return ""

        return result + "m\\W"

    def get_prompt_color(self) -> str:
        return self.__prompt_color

    def get_prompt_bg(self) -> str:
        return self.__prompt_bg

    def get_prompt_style(self) -> str:
        return self.__prompt_style

    def set_prompt_color(self, color: dict[str]) -> None:
        if "color" in color.keys():
            self.__prompt_color = color["color"]
        if "bg" in color.keys():
            self.__prompt_bg = color["bg"]
        if "style" in color.keys():
            self.__prompt_style = color["style"]

    def get_code_prompt(self) -> str:
        result: str = "\\e["
        if self.get_prompt_bg() != "":
            result += f"{BACKGROUND_COLORS[self.get_prompt_bg()]};"
        if self.get_prompt_color() != "":
            result += f"{COLORS[self.get_prompt_color()]};"
        if self.get_prompt_style() != "":
            result += f"{TEXT_FORMAT[self.get_prompt_style()]}"

        if result == "\\e[":
            return ""

        return result + "m "

    def get_bashrc_content(self) -> str:
        return f"""
# BasteRC - A simple modifyable RC file for bash
# Author : Valentin Thuillier <@luxferre-code>
PS1="{self.get_code_user()}@{self.get_code_host()}:{self.get_code_path()}${self.get_code_prompt()}"
"""

    def add_alias(self, alias: dict[str, str]) -> None:
        assert "name" in alias.keys(), "Alias must have a name"
        assert "value" in alias.keys(), "Alias must have a value"
        self.__alias[alias["name"]] = alias["value"]

    def get_alias(self) -> dict[str, str]:
        return self.__alias

    def get_alias_content(self) -> str:
        result: str = ""
        for name, value in self.get_alias().items():
            result += f"alias {name}='{value}'\n"
        return result
