import re

from typing_extensions import overload
class Scanner:
    """
    """
    __startingState: str = "START"
    __accepting_states: (str) =\
    (
        "LBRACK", "RBRACK", "MINUS", "PLUS", 
        "NUMERIC", "COMMA", "EXPO", "WHITESPACE"
    )
    __transitions =\
    {
        "START": 
        {
            #operators that can be at the beginning
            # use class types instead
            "(":"LBRACK",
            ")":"RBRACK",
            "**":"POW",
            "/":"DIVIDE",
            "*":"MUL",
            "+":"PLUS",
            "-":"MINUS",
            " ":"WHITESPACE",
            ".":"DOT",
            "=":"ASSIGN",


            # numerics can always be at the beginning
            "0":"NUM", "1":"NUM", "2":"NUM", "3":"NUM", "4":"NUM",
            "5":"NUM", "6":"NUM", "7":"NUM", "8":"NUM", "9":"NUM"
        }
    }

    def __init__(self, expr: str):
        self.__word = str(expr)
        self.__stack: LifoQueue = LifoQueue()
        

    """
    """
    def scanLine(self) -> None:
        self.__stack: stack = stack[int]()

        for ch in self.__word:
            self.__transitions["START"][ch]
            print(str("{} ").format(self.__transitions["START"][ch]), end=' ')
        print()



class CFG:
    """
    Math expression evaluator
    """
    def __init__(self, expr: [str]):
        self.__grammar =\
        {
        #    "start":    [
        #                    ["expr"]
        #                ],
        #    "expr":    [
        #                    ["mulexpr"], 
        #                    ["mulexpr", {"addop", "mulexpr"}]
        #                ],
        #    "mulexpr":  [
        #                    ["mulexpr"], 
        #                    ["powexpr", {"mulop", "powexpr"}]
        #                ],
        #    "powexpr":  [
        #                    ["-", "powexpr"], 
        #                    ["+", "powexpr"], 
        #                    ["atom", ["**", "powexpr"]]
        #                ],
        #    "atom":     [
        #                    ["identifier", ["(", "expr", ")"]],
        #                    ["numeric"],
        #                    ["(", "expr", ")"]
        #                ],
        #    "numeric":  [
        #                    ["/[0-9]+(\.[0-9]*)?([eE][\+\-]?[0-9]+)?/"]
        #                ],
        #    "ident":    [
        #                    ["/[A-Za-z_][A-Za-z_0-9]/"]
        #                ],
        #    "mulop":    [
        #                    ["/"],
        #                    ["*"]                   
        #                ],
        #    "addop":    [
        #                    ["+"], 
        #                    ["-"]
        #                ]
        }

    def parse(self) -> bool:
        ...


class EE(Scanner, CFG):
    ...
