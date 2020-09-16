"""
Web Scrapping
=============
#### Author: `Daniel Herrera`
#### Description:: 
"""

from bs4 import BeautifulSoup as _BeautifulSoup
import requests as _request
from urllib.parse import urlparse as _urlparse
from colorama import (Fore, Back, Style, init); init()
from html.parser import HTMLParser as _HTMLParser


class MyHTMLParser(_HTMLParser):
    """
    Web Scrapper
    ============
    """
    from html.entities import name2codepoint as __name2codepoint
    def handle_starttag(self, tag, attrs):
        print(Back.WHITE, Fore.BLACK,"Start tag |", tag, Style.RESET_ALL)
        for attr in attrs:
            print("     attr |", attr)

    def handle_endtag(self, tag):
        print(Back.WHITE, Fore.BLACK,"End tag   |", tag, Style.RESET_ALL)

    def handle_data(self, data):
        print(Back.BLACK, Fore.LIGHTGREEN_EX,"Data      |", data, Style.RESET_ALL)

    def handle_comment(self, data):
        print("Comment   |", data)

    def handle_entityref(self, name):
        c = chr(self.__name2codepoint[name])
        print("Named ent |", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent   |", c)

    def handle_decl(self, data):
        print("Decl      |", data)