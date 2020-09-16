"""
Data Structures In Python
=========================
#### Author: `Daniel Herrera`
#### Description:: 
"""

class constack():
    """
    Contiguous Stack
    =====
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


class BinByte(int):
    from math import floor as __floor
    #init
    def __init__(self, num_value: (int or str) = "5" or 5):
        # feilds
        self.__binary_rep = list("{0:b}".format(num_value))
        self.__data: list = []
        self.toBinary()

    def toBinary(self): # TODO: COMMENT THE FUNCTION
        # finding length of bits
        """
        if (cbl_len := len(self.__binary_rep)) % 8 != 0:
            cbl_needed = 8 - cbl_len 
            #constant time loop
            for i in range(cbl_needed): 
                self.__binary_rep.insert(0, R"0")
            for shell in shortChuncks(self.__binary_rep, 8, direction=1):
                for i,root in enumerate(shell):
                    shell[i]
                self.__data.append()
        else:
            for i in shortChuncks(self.__binary_rep, 8, direction=1):
                self.__data.append("{}".format("".join(i)))
        """
    
    @staticmethod 
    def bytes_mat(raw_string_rep):
        ...

    @property
    def data(self): return self.__data

    def __str__(self):
        ss = " ".join(self.__data)
        return ss

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


