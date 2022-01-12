from os import system
from variables import Variables
from plot import Plot

operators = ["sys", "var", "function", "read", "print", "println"]
operands = ["+", "-", "*", "/", "(", ")"]

class Execute:
    def exe(inp, vars, functions, os):
        splits = inp.split()
        if splits[0] == "input":
            vars[splits[1]] = input()
            return
        elif splits[0] == "//":
            return
        elif splits[0] == "print":
            if inp[6:] in vars:
                print(vars[inp[6:]], end="")
            else:
                print(inp[6:], end="")
            return
        elif splits[0] == "println":
            if inp[8:] in vars:
                print(vars[inp[8:]])
            else:
                print(inp[8:])
            return
        elif inp == "quit":
            quit()
        elif splits[0] == "display":
            Plot.plot(functions[splits[1]][1], Variables.filterVars(functions[splits[1]][0], vars, True), vars)
            return
        elif splits[0] == "function":
            try:
                functions[splits[1]] = [Variables.filterVars(splits[3], vars, True), splits[4]]
            except:
                functions[splits[1]] = [Variables.filterVars(splits[3], vars, True), 5]
            return
        elif inp == "clear":
            if os == "Windows":
                system('cls')
            else:
                system("clear")
            return
        elif splits[0] == "sys":
            system(inp[4:])
            return
        elif splits[0] == "var":
            try:
                if splits[1] in operators or splits[1] in operands:
                    print("Error: variable name defined as keyword")
                vars[splits[1]] = eval(Variables.filterVars(splits[3], vars, False))
            except:
                print("Error: undefined side")
            return
        elif splits[0] == "endif":
            return
        try:
            print(eval(Variables.filterVars(inp, vars, False)) if inp not in vars else print(1/0))
        except:
            print("Error: invalid operation")