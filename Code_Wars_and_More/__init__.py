"""
Main method and testing
"""
# importing modules
from pysbox.testingallcode import *
import pysbox.sandbox.sandbox_methods as sbm
import pysbox.kata.katas_methods as ktm

def main(*args: str) -> None:
    #sbm.sandycanvas()
    print(ktm.HammingCode.encode("hey"))
    # for i in range(len(ktm.HammingCode.encode("hey"))):
    #     print(ktm.HammingCode.decode(ktm.HammingCode.encode("hey")))

    import requests as _req
    parser = sbm.MyHTMLParser()
    resp = _req.get("https://partnaranimalhealth.ca/")
    print(parser.feed(resp.text))

# main method
if __name__ == "__main__":
    main()
    ut.main()
