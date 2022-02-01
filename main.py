from vintro import VIntro
INTRO = VIntro.intro()
print(INTRO)
from input import Input

vars = {}
functions = {}

Input.loop(vars, functions, VIntro.os())