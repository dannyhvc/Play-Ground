"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Author: Daniel Herrera - Vazquez
Date: Nov 20, 2019
Desc: Simple program that prints all illegible chars until
      it matches the correct chars.

      (note): this is my custom interpretation of a program I     
              saw on reddit's r/Python sub-reddit.                
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""         
                                                                  
# importing pythons libs
import random as r  
#import numpy as np
                                                                  
# return the amount of hits of a recurrent object in a list
def duplicates(lst : list, item : object) -> list:                                        
    return [i for i, x in enumerate(lst) if x == item]              
                                                                  
                                                                  
# does a cool matrix print for any line typed in
def cool_print(sstream: str) -> None:
    charReadables = [chr(asc) for asc in range(33, 176 + 1)]
    coolLine = [""] * len(sstream)
    hits = duplicates(list(sstream), ' ') 
    idx = 0

    while True:
        for i in range(idx, len(coolLine)):
            coolLine[i] = r.choice(charReadables)
        for indexs in hits: coolLine[indexs] = ' '
        # prints the product of the cool print
        if idx == len(coolLine): 
            print("-->",''.join(coolLine[:]), end="\n")
            break
        elif coolLine[idx] == sstream[idx]:
            #coolLine[idx] = ' ' # this is only used to see the shape.
            idx += 1
        print("-->",''.join(coolLine[:]), end="\r", flush=True)

        
if __name__ == '__main__': 
    cool_print(str(input("[Enter a line that you want to matrix print]""\n>>> ")))