"""##########################################################################
|   Author:                                                                 |
|       ____              _      __   __  __                                |                           
|      / __ \____ _____  (_)__  / /  / / / /__  _____________  _________ _  |
|     / / / / __ `/ __ \/ / _ \/ /  / /_/ / _ \/ ___/ ___/ _ \/ ___/ __ `/  |
|    / /_/ / /_/ / / / / /  __/ /  / __  /  __/ /  / /  /  __/ /  / /_/ /   |
|   /_____/\__,_/_/ /_/_/\___/_/  /_/ /_/\___/_/  /_/   \___/_/   \__,_/    |
|                                                                           |
|   Date:   Apr 10, 2019                                                    |
##########################################################################"""
# imports
import enum as _enum
import turtle as _turtle


from colorama import (Fore, Back, Style, init); init()

def findAll(l: list, val: object) -> list:
    return [i for i in range(len(l)) if l[i] == val]

def numberOfOccurence(l: list, val: object) -> int:
    return len(findAll(l, val))

def nats(n: int):
    yield nats(n)
    yield from nats(n+1)

def seive(s):
    n = next(s)
    yield n
    yield from seive(i for i in s if i%n != 0)

def longChuncks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def shortChuncks(lst, n):
    """returns successive n-sized chunks from lst."""
    return [lst[i:i+n] for i in range(0, len(lst), n)]

class typename:
    def __init__(self, type_alias: str = 'T'):
        self.__typeAlias = type_alias

    @property
    def __class__(self):
        return self.__typeAlias
    
    
class template(typename):
    """
    This class is used to immitate the following:
    template <typename _Ty>
    ...

    which in turn is the generic representation of a class.
    Python built-in duck-typing provides for dynamic type although
    this creates issues when trying to enforce and formalize code.
    the typing module has attempted in creating this same templated
    generic argumenting.

    consider the following:
    from typing import Generic, TypeVar

    T = TypeVar('T')
    class foo(Generic[T]): 
        pass

    x = foo()[int]

    this is somewhat cryptic in my opinion and makes it so that programmers
    that have tried implement type protection 
    """
    def __init__(self): 
        self.__newType: typename = None

    def __getitem__(self, _Ty: typename):
        self.__newType = _Ty
  
    def __call__(self, *params): 
        if any([isinstance(i, str) for i in params]): 
            raise TypeError("parameter cannot be a string !!") 
        else: 
            return self.function(*params) 


class stack():
    """
    """
    def __init__(self, *args):
        """Default constructor with param pack."""
        self.__container: list = list(args)

    def empty(self) -> bool:
        """Returns the true if container has more than zero elements"""
        return self.size() == 0

    def push(self, item) -> None:
        """Is the same as push_back in c++ vector container"""
        self.__container.append(item)

    def pop(self) -> object:
        if self.empty():
            return None
        return self.__container.pop()

    def size(self) -> int:
        return len(self.__container)

    def __str__(self) -> str:
        return super().__str__(self.__container)

    def __add__(self, s):
        return self.__container + s.__container

    def __repr__(self):
        storage_str: str = str()
        for x in self.__container:
            if x != self.__container[-1]:
                storage_str += str("{}, ").format(x)
            else:
                storage_str += str("{} \n").format(x)
        return str("{}").format(storage_str)

    def __getitem__(self, index: int):
        if len(self.__container) >= index:
            raise IndexError("Index Out of Bounds")
        return self.__container[index]


"""#################################################
| ______  __ __  ____  ______  __ __  _        ___ |    
||      ||  |  ||    \|      ||  |  || |      /  _]|      
||      ||  |  ||  D  )      ||  |  || |     /  [_ |    
||_|  |_||  |  ||    /|_|  |_||  |  || |___ |    _]|    
|  |  |  |  :  ||    \  |  |  |  :  ||     ||   [_ |    
|  |  |  |     ||  .  \ |  |  |     ||     ||     ||    
|  |__|   \__,_||__|\_| |__|   \__,_||_____||_____||    
|                                                  |  
#################################################"""
def pick_turt_drag(turt: _turtle.Turtle):
    def dragging(x: float, y: float):
        turt.ondrag(None)
        turt.setheading(turt.towards(x, y))
        turt.goto(x, y)
        turt.ondrag(dragging)
    return dragging

def sandycanvas():
    # _turtle.begin_fill() # start the drawing
    ########################################
    screen = _turtle.Screen()
    frank = _turtle.Turtle('turtle')
    frank.speed("fastest")
    frank.ondrag(pick_turt_drag(frank))
    ########################################
    # _turtle.end_fill() # end the drawing
    # _turtle.done()
    screen.mainloop()


"""########################################################################
| __          __  _        _____                            _             |
| \ \        / / | |      / ____|                          (_)            |
|  \ \  /\  / /__| |__   | (___   ___ _ __ __ _ _ __  _ __  _ _ __   __ _ |
|   \ \/  \/ / _ \ '_ \   \___ \ / __| '__/ _` | '_ \| '_ \| | '_ \ / _` ||
|    \  /\  /  __/ |_) |  ____) | (__| | | (_| | |_) | |_) | | | | | (_| ||
|     \/  \/ \___|_.__/  |_____/ \___|_|  \__,_| .__/| .__/|_|_| |_|\__, ||
|                                              | |   | |             __/ ||
|                                              |_|   |_|            |___/ |
########################################################################"""
from html.parser import HTMLParser as _HTMLParser
from html.entities import name2codepoint as _name2codepoint
import os as _os

class MyHTMLParser(_HTMLParser):
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
        c = chr(_name2codepoint[name])
        print("Named ent |", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent   |", c)

    def handle_decl(self, data):
        print("Decl      |", data)
