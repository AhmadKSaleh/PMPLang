import platform
from variables import Variables 

# vintro stands for version and introduction

class VIntro:
    def intro():
        return f"""PMPL Version 3.0 Badlands for {platform.system()}
Python Interpreter Version {platform.python_version()}
Press Ctrl+C to exit or type 'quit'
"""
    def os():
        return platform.system()

    def veval(x, vars, isFunc):
        return eval(Variables.filterVars(x, vars, isFunc))
    