import platform

# vintro stands for version and introduction

class VIntro:
    def intro():
        return f"""PMPL Version 2.5 Savanna for {platform.system()}
Python Interpreter Version {platform.python_version()}
Press Ctrl+C to exit or type 'quit'
"""
    def os():
        return platform.system()
    