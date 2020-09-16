"""
SandBox Methods
===============
#### Author: `Daniel Herrera`
#### Description:: 
collection of methods and tools to moderate the

"""
### imports
from pysbox.__imports__ import _typing
_Any = _typing.Any
_List = _typing.List

def findAll(l: _List[_Any], val: object) -> list:
    """
    findAll
    =======
    `params`::
    `returns`::
    """
    return [i for i in range(len(l)) if l[i] == val]

def numberOfOccurence(l: _List[_Any], val: object) -> int:
    return len(findAll(l, val))

def nats(n: int):
    yield nats(n)
    yield from nats(n+1)

def seive(s):
    n = next(s)
    yield n
    yield from seive(i for i in s if i%n != 0)

def longChuncks(lst: _List[_Any], n: int, direction: int=1):
    """Yield successive n-sized chunks from lst."""
    switch = {
        1: (lst[i:len(lst)-1] 
            if i+n > len(lst)-1 
            else lst[i:i+n] 
            for i in range(0, len(lst), n)),
        # reverses the list order and the element order
        -1: (lst[0:i][::-1] 
             if i-n < 0 
             else lst[i-n:i][::-1] 
             for i in range(len(lst), 0, -n))
    }
    return switch[direction]

def shortChuncks(lst:_List[_Any], n: int, direction: int=1):
    """returns successive n-sized chunks from lst."""
    switch = { 
        1: [lst[i:len(lst)-1]
            if i+n > len(lst)-1 
            else lst[i:i+n] 
            for i in range(0, len(lst), n)],
        # reverses the list order and the element order
        -1: [lst[0:i][::-1] 
             if i-n < 0 
             else lst[i-n:i][::-1] 
             for i in range(len(lst), 0, -n)]
    }
    return switch[direction]

def calltracker(func):
    """
    calltracker
    ============
    decorator to analyze when a function has been called
    """
    import functools as __functools
    @__functools.wraps(func)
    def wrapper(*args):
        wrapper.has_been_called = True
        return func(*args)
    wrapper.has_been_called = False
    return wrapper