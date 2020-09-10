""" unittest package for
Name: Daniel Herrera
"""

# imports
import unittest

# kata mods
from pysbox.kata.katas_methods import *
from pysbox.kata.automaton import *
from pysbox.kata.fullMetalChemist import *

# sandbox mods
from pysbox.sandbox.sandbox_methods import (
    findAll,
    numberOfOccurence,
    #DISPATCHER,
    stack,
    #Scanner,
    #CFG,
    #EE,
    nats,
    seive
)


class sandbox_methods_ut(unittest.TestCase):
    """ This class will test all the methods within the 
        sandbox package including any classes and the sub classes of the
        sandbox package.
    """

    def control_test(self) -> int:
        """Control test code to set the standard for accepted state output. """
        return 0

    def test_findAll(self) -> bool:
        """ Test the indexes fo the hits given
            Hits should be a list of indexs given the 
            value wanted. 
        """
        return self.assertEqual(list([4,5]), findAll(list([1,2,3,4,5,5]), 5))

    def test_numberOfOccurence(self) -> bool:
        """ Using the findAll tool method to return the list
            and find the size.
        """
        return self.assertEqual(2, numberOfOccurence(list([1,2,3,4,5,5]), 5))

    def test_stack_init(self) -> None:
        """
        """
        s = stack("a","b","c","d")
        return

    def test_stack_empty(self):
        """ Assertion that the stack is not empty. """
        return self.assertTrue(stack().empty())

    def test_stack_push(self):
        stack().push(1)     
        
    def test_primeNum(self):
        n = seive(nats(2))
        return n


