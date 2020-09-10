import unittest as ut

class ParseHer(object):
    """
    To do that, you'll have to accomplish two tasks:

    Find a way to properly tokenize and then parse the name of the molecule, using the provided information (you'll have to find out the proper grammar, like I did ;-p ).
    Then build the complete raw formula and return it as a dictionary (key: chemical symbol as a string, value: number of this chemical element in the molecule).
    All inputs will be valid.


    To help you in this task, several things are provided:

    No chemistry knowledge is required: you'll find all the needed information below. (Note: it's very long, yes, but a large majority of the strings needed are already provided in the solution setup, using different lists. Use them as you want )
    To build the raw formula, being a chemist might be of some help, but don't worry if you are not: you'll just have to identify the patterns through the different tests. They are specifically designed so that these patterns can be found easily. (Note: the related academical knowledge is about "degrees of insaturation" of the molecule, if you're interested in it. If you already know that, that will of course be of help, but if you do not, just focus yourself on the pattern recognition work, going through the sample tests, rather than trying to understand the notion with the wiki article (which is pretty bad about that ))
    All the molecules will be drawn in the console (except for the random tests and the very last fixed tests), so that you can see what it is exactly. (Note: due to the need of escape characters '' to represent some bounds, the strings in the example tests might not be very readable. Prefer to look at the version printed in the console )

    Specifications of the tests:
    40 sample tests
    around 85 fixed tests
    6000 random tests
    """
    # Number:                   1         2        3...
    RADICALS    = [['meth'], ['eth'], ['prop'], ['but'], ['pent'], ['hex'], ['hept'], ['oct'], 
                            ['non'], ['dec'], ['undec'], ['dodec'], ['tridec'], ['tetradec'], ['pentadec'], 
                            ['hexadec'], ['heptadec'], ['octadec'], ['nonadec']]
  

    MULTIPLIERS = [['di'], ['tri'], ['tetra'], ['penta'], ['hexa'], ['hepta'], ['octa'], 
                            ['nona'], ['deca'], ['undeca'], ['dodeca'], ['trideca'], ['tetradeca'], 
                            ['pentadeca'], ['hexadeca'], ['heptadeca'], ['octadeca'], ['nonadeca']]

    
    SUFFIXES    = [['ol'], ['al'], ['one'], ['oic acid'], ['carboxylic acid'], ['oate'], 
                            ['ether'], ['amide'], ['amine'], ['imine'], ['benzene'], ['thiol'], 
                            ['phosphine'], ['arsine']]


    PREFIXES    = [['cyclo'], ['hydroxy'], ['oxo'], ['carboxy'], ['oxycarbonyl'], 
                            ['anoyloxy'], ['formyl'], ['oxy'], ['amido'], ['amino'], ['imino'], 
                            ['phenyl'], ['mercapto'], ['phosphino'], ['arsino'], ['fluoro'], 
                            ['chloro'], ['bromo'], ['iodo']]


    CHAIN_END   = [["ane"], ["ene"], ["yne"]] 

    TERMINALS   = [["-"],[","],["("],[")"],[""]]


    basic_chemical = [["rad","position_list","stops"]]

    # Note that alkanes, alkenes, alkynes, and akyles aren"t present in these lists
    def __init__(self, name: str):
        # Do whatever you want, here....
        self.__name: str = str(name).lower()
        self.__chemStruct: dict = {'C': 0, 'H': 0, 'O': 0}
        #self.CFG_id: dict = {
        #    "rad" : RADICALS,
        #    "mulp" : MULTIPLIERS,
        #    "suff" : SUFFIXES,
        #    "pref" : PREFIXES,
        #    "chainEnd" : CHAIN_END,
        #    "stops": TERMINALS
        #}


    def parse(self) -> dict:
        '''
        Parse the name given as argument in the constructor, and 
        output the dict representing the raw formula

        ### pos_list"-"multip Rad pos_listchemEnd[pos_list]"-"suff
        >   Terminals ::= Epsilon | "-" | ","
        >   pos ::= [1,19]
        >   pos_list ::= pos_list","pos | pos | Epsilon
            
        >   basic_chemical ::= Rad chainEnd | Rad"ane"
        >   basic_chemical ::= Rad"-"pos_list"-"chainEnd | basic_chemical
        '''
        #basic_chemical = \
        #    self.CFG_id["rad"] + self.CFG_id["chainEnd"]
        return self.__chemStruct



class Test_FMC(ut.TestCase):
    """
    """
    def test_basic_chemical(self) -> None:
        self.assertEqual
        (
            ParseHer("methane").parse(), 
            {"C":1, "H":3, "O":0}
        )

    def test_position_list(self) -> None:
        self.assertEqual
        (
            ParseHer("but-1,3-ene").parse(), 
            {"C":4, "H":8, "O":0}
        )