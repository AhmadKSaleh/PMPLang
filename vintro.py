import platform
from variables import Variables 
from termcolor import colored

# vintro stands for version and introduction

class VIntro:
    def intro():
        python = platform.python_version_tuple()
        if int(python[1]) < 10:
            print(colored("\nERROR: Upgrade to python version >3.10 to use the programming language!\nIf you got this message and you have version >3.10, send us a github issue!", "red")) # make sure the user has the required python version
            quit()
        return f"PMPL Version 3.1 Badlands for {platform.system()}\nPython Interpreter Version {platform.python_version()}\nPress Ctrl+C to exit or type 'quit'\n"
    def os():
        return platform.system()

    def veval(x, vars, isFunc):
        return eval(Variables.filterVars(x, vars, isFunc))
    