from os import system
from variables import Variables
from readfile import ReadFile
from plot import Plot
from vintro import VIntro

operators = ["sys", "var", "function", "read", "print", "println"]
operands = ["+", "-", "*", "/", "(", ")"]

INTRO = VIntro.intro()

class Input:
    def loop(vars, functions, os):
        while True:
            try:
                inp = input(">>> ")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()
            splits = inp.split()
            if splits[0] == "input":
                vars[splits[1]] = input()
                continue
            elif splits[0] == "//":
                continue
            elif splits[0] == "print":
                if inp[6:] in vars:
                    print(vars[inp[6:]], end="")
                else:
                    print(inp[6:], end="")
                continue
            elif splits[0] == "println":
                if inp[8:] in vars:
                    print(vars[inp[8:]])
                else:
                    print(inp[8:])
                continue
            elif inp == "quit":
                print("Goodbye!")
                quit()
            elif splits[0] == "display":
                Plot.plot(functions[splits[1]][1], functions[splits[1]][0], vars)
                continue
            elif splits[0] == "function":
                try:
                    functions[splits[1]] = [Variables.filterVars(splits[3], vars, True), splits[4]]
                except:
                    functions[splits[1]] = [Variables.filterVars(splits[3], vars, True), 5]
                continue
            elif splits[0] == "read":
                try:
                    ReadFile.loop({}, splits[1], {}, os)
                except:
                    print("Error: too many file calls")
                continue
            elif inp == "clear":
                if os == "Windows":
                    system('cls')
                else:
                    system("clear")
                print(INTRO)
                continue
            elif splits[0] == "sys":
                system(inp[4:])
                continue
            elif splits[0] == "var":
                try:
                    if splits[1] in operators or splits[1] in operands:
                        print("Error: variable name defined as keyword")
                    vars[splits[1]] = eval(Variables.filterVars(splits[3], vars, False))
                except:
                    print("Error: undefined side")
                continue
            try:
                print(eval(Variables.filterVars(inp, vars, False)))
            except:
                print("Error: invalid operation")