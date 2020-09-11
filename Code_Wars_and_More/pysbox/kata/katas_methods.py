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
import numpy as _np
import enum as _enum
from fractions import Fraction as _Fraction


def spin_words(sentence: str) -> str:
    """
    Reverses each word within a given sentence.
    Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"  
    """
    result = ""
    for e in sentence.split(' '): result += "{} ".format(e[::-1])
    return result

def bernoulli_number(n):
    '''
    this function returns a bernoulli (B_n) number given n
    '''
    if n == 1:
        return _Fraction(-1,2)
    A = [0] * (n+1)
    for m in range(n+1):
        A[m] = _Fraction(1, m+1)
        for j in range(m, 0, -1):
            A[j-1] = j*(A[j-1] - A[j])
    return A[0] # (which is B_n)


class HammingCode:
    from pysbox.sandbox.sandbox_methods import shortChuncks as __wedges
    """
    Data error correction and provention algorithm
    eg. hey -> 104 101 121
            -> 01101000 01100101 01111001
            -> 011010000110010101111001
        with hamming correction
            -> 000111111000111000000000000111111000000111000111000111111111111000000111
    one = 111
    zero = 000
    """
    class __bitNum(_enum.Enum): off = 0; on = 1      

    @staticmethod
    def encode(string: str) -> str:
        """
        """
        # breaking the string into a ascii index array 
        ordinalEncoder = [ord(ch) for ch in string]       
        # turing each ascii num into a binary rep
        binaryEncoder = [str(bin(num).replace("0b", "0")) for num in ordinalEncoder]
        # cycling through the 
        hammingEncoder: str = str()
        # cycling through bytes of the ascii reps
        for bin_str in binaryEncoder:
            # getting each bit and tripling the char to immitate hamming algo
            for ch in bin_str:
                hammingEncoder += (str(ch)*3)
        return hammingEncoder

    @staticmethod
    def decode(bits: str) -> str:
        """
        Revise Decoding and ending.
        NOTE: date 09/10/2020
        """
        print(bits) # TODO:TODO: TAKE THE PRINT AWAY
        # creates an evenly divided list of chuncks from a
        #  given list and divisor
        if len(bits) % 3 != 0: # if false then the data is corupted
            raise Exception("Invalid data: data may be corrupted...")

        hammingDecoder = [
            block for block in HammingCode.__wedges(bits, 3)
                         ]
        message: str = str()
        for i,n in zip(
            hammingDecoder, 
            range(len(hammingDecoder))):
            __x: list = [int(x) for x in list(i)]
            if (n % 8 == 0) and (n != 0):
                message += ' '
            if sum(__x) > 1:
                message += '1'
            else:
                message += '0'
        del hammingDecoder
        char_list = [
            chr(int(_, base=2)) if _ != "00100000" else chr(' ')\
            for _ in message.split(' ')
                    ]
        print(char_list) # TODO:TODO: TAKE THE PRINT AWAY
        return "".join(char_list)