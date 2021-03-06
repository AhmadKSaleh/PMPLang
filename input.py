from os import system
from variables import Variables
from readfile import ReadFile
from plot import Plot
from vintro import VIntro
from termcolor import colored

operators = ["sys", "var", "function", "read", "print", "println"]
operands = ["+", "-", "*", "/", "(", ")"]
if_perands = ["==", "!=", ">=", "<=", ">", "<"]
varTypes = ['int', 'str', 'bool']

secret = "NTYgNkQgMzEgNzMgNTEgMzIgNEUgNTggNTUgNkUgNTIgNTggNjEgNkIgNUEgNEIgNTUgNkQgNzggNzMgNjIgNkMgNkMgNTggNEQgNDQgNDYgNjkgNTYgNTcgNzggNEEgNTYgNDcgMzEgMzQgNjEgNkQgNEEgNzIgNjEgN0EgNkIgM0Q+-="
end = "54 68 65 20 73 65 63 72 65 74 73 20 68 61 76 65 20 62 65 65 6E 20 73 68 6F 77 6E 2C 20 61 6C 74 68 6F 75 67 68 20 6E 6F 74 20 74 68 65 6D 20 61 6C 6C 2E"

INTRO = VIntro.intro()

class Input:
    def loop(vars, functions, os):
        pastOperationSuccess = True
        if open("secret.txt", "r").readline() == "1":
            print(secret)
            print(end)
            quit()
        while True:
            try:
                if pastOperationSuccess:
                    inp = input(colored(">>> ", "green"))
                else:
                    inp = input(colored(">>> ", "red"))
                    pastOperationSuccess = True
            except KeyboardInterrupt:
                print("\nError: user force-exited, ending process")
                quit()
            splits = inp.split()
            try:
                if splits[1] in if_perands:
                    a = eval(Variables.filterVars(splits[0], vars, False))
                    b = eval(Variables.filterVars(splits[2], vars, False))
            except:
                None
            if splits[0] == "input":
                vars[splits[1]] = input()
                continue
            elif splits[0] == "inputASCII":
                vars[splits[1]] = ord(input())
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
                print("Error: user force-exited, ending process")
                quit()
            elif splits[0] == "display":
                Plot.plot(functions[splits[1]][1], functions[splits[1]][0], vars)
                continue
            elif splits[0] == "display3d":
                Plot.plot3d(functions[splits[1]][1], Variables.filterVars(functions[splits[1]][0], vars, True), vars)
                continue
            elif splits[0] == "function":
                try:
                    functions[splits[1]] = [splits[3], splits[4]]
                except:
                    functions[splits[1]] = [splits[3], 5]
                continue
            elif splits[0] == "derivative":
                    if splits[2] == "->":
                        try:
                            functions[splits[3]] = [Plot.derivative(functions[splits[1]][0], vars), functions[splits[1]][1]]
                        except:
                            functions[splits[3]] = [Plot.derivative(functions[splits[1]][0], vars), 5]
                    else:
                        print("Error: while calculating derivative of " + splits[1])
                        pastOperationSuccess = False
                    continue
            elif splits[0] == "read":
                try:
                    ReadFile.loop({}, splits[1], {}, os)
                except:
                    print("Error: while reading " + splits[1])
                    pastOperationSuccess = False
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
            elif splits[0] in varTypes:
                try:
                    if splits[1] in operators or splits[1] in operands:
                        print("Error: variable name defined as keyword")
                        pastOperationSuccess = False
                    vars[splits[1]] = [eval(Variables.filterVars(splits[3], vars, False)), splits[0]]
                except:
                    print("Error: while processing variable " + splits[1])
                    pastOperationSuccess = False
                continue
            try:
                match splits[1]:
                    case "==":
                        print(a == b)
                        continue
                    case ">=":
                        print(a >= b)
                        continue
                    case "<=":
                        print(a <= b)
                        continue
                    case "!=":
                        print(a != b)
                        continue
                    case ">":
                        print(a > b)
                        continue
                    case "<":
                        print(a < b)
                        continue
            except:
                None
            if inp == "Show me the secrets, behind this big big wall.":
                print(secret)
                print(end)
                secrets = open("secret.txt", "r+")
                secrets.write("1")
                quit()
            try:
                print(eval(Variables.filterVars(inp, vars, False)))
            except:
                print("Error: invalid operation: " + splits[0])
                pastOperationSuccess = False