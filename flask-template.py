#Janet Zhang
#Pd 6 SoftDev DW
#Work 2: fill up your flask

from flask import Flask

janet= Flask(__name__)

@janet.route("/")


def home() : 
    return __name__ + "\tHello World"


@janet.route("/map")
def map() :
    return __name__ + "\tmap"


@janet.route("/drive")
def drive() :
    return __name__ + "\tdrive"


if __name__ == "__main__": 
    janet.run()
