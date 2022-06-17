#!/usr/bin/python3
import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable()
def name_check(name):
    if len(name)<2:
        logging.debug("checking of thelength")
        return "invalid"
    elif name.isspace():
        print("checking if name in space")
        return "invalid"
    elif name.isalpha():
        print("checking if a name is alphabet")
        return "valid"
    elif name.replace(" ","").isalpha():
        print("checking for full name")
        return "vaid"
    else:
        print("failed")
        return "invalid"
print(name_check("alexander123"))
     

