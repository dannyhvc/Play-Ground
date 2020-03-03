"""
Author: Daniel Herrera
Date: Feb 15, 2020

Version 1 - Added {bitCounting, duplicate_count}
            implmented version control and kata
            function monitoring.
"""

def bitCounting(n:int) -> int: 
    return bin(10)[:2].count('1')

def duplicate_count(text : str) -> int:
    charMap: dict = {}
    for ch in text.upper():
        if ch not in charMap:
            charMap.update({ch : text.upper().count(ch)})  


