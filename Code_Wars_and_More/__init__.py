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
# importing modules
from pysbox.testingallcode import *
import pysbox.sandbox.sandbox_methods as sbm
import pysbox.kata.katas_methods as ktm

def main(*args: str) -> None:
    # sbm.sandycanvas()
    hcode_e: str = ktm.HammingCode.encode("D A N")
    hcode_d: str = ktm.HammingCode.decode(hcode_e)
    #print(hcode_e)
    print(hcode_d) 

    """
        import requests as _req
        parser = sbm.MyHTMLParser()
        resp = _req.get("https://partnaranimalhealth.ca/")
        print(parser.feed(resp.text))
    """

# main method
if __name__ == "__main__":
    main()
    ut.main()