from input import Input
from vintro import VIntro

INTRO = VIntro.intro()
print(INTRO)

vars = {}
functions = {}

Input.loop(vars, functions, VIntro.os())