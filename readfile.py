from os import system
from executeLine import Execute
from variables import Variables
from plot import Plot
from label import Label

operators = ["sys", "var", "function", "read", "print", "println"]
operands = ["+", "-", "*", "/", "(", ")"]

class ReadFile:
    def loop(vars, fileName, functions, os):
        # isIf = [False, 0, 0]
        # exeLines = []
        # executeIf = False
        file = open(fileName, 'r')
        lines = file.readlines()
        lines = [line.replace("\n", "") for line in lines]
        for inp in lines:
            splits = inp.split()
            # if inp in exeLines:
            #     continue
            # if splits[0] == "if":
            #     labels = Label.labelFile(fileName)
            #     for label in labels:
            #         if label[0] == "if":
            #             isIf = [True, label[1], label[2]]
            #             if splits[2] == "==":
            #                 if eval(Variables.filterVars(splits[1], vars, False)) == eval(Variables.filterVars(splits[3], vars, False)):
            #                     executeIf = True
            #             elif splits[2] == ">":
            #                 if eval(Variables.filterVars(splits[1], vars, False)) > eval(Variables.filterVars(splits[3], vars, False)):
            #                     executeIf = True
            #             elif splits[2] == "<":
            #                 if eval(Variables.filterVars(splits[1], vars, False)) < eval(Variables.filterVars(splits[3], vars, False)):
            #                     executeIf = True
            #             elif splits[2] == ">=":
            #                 if eval(Variables.filterVars(splits[1], vars, False)) >= eval(Variables.filterVars(splits[3], vars, False)):
            #                     executeIf = True
            #             elif splits[2] == "<=":
            #                 if eval(Variables.filterVars(splits[1], vars, False)) <= eval(Variables.filterVars(splits[3], vars, False)):
            #                     executeIf = True
            #         if label[0] == "endif" and isIf[0] and isIf[2] == label[2] and executeIf:
            #             from_ = isIf[1] + 1
            #             to = label[1]
            #             exeLines = lines[from_:to]
            #             for line in exeLines:
            #                 Execute.exe(line, vars, functions, os)
            #             isIf = [False, 0, 0]
            #         else:
            #             executeIf = False
            #     continue
            # Work on this later! (or implement another function to make this language turing complete)
            # TODO: @AhmadKSaleh
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
                quit()
            elif splits[0] == "display":
                Plot.plot(functions[splits[1]][1], Variables.filterVars(functions[splits[1]][0], vars, True), vars)
                continue
            elif splits[0] == "function":
                try:
                    functions[splits[1]] = [Variables.filterVars(splits[3], vars, True), splits[4]]
                except:
                    functions[splits[1]] = [Variables.filterVars(splits[3], vars, True), 5]
                continue
            elif splits[0] == "read":
                try:
                    ReadFile.loop({}, splits[1], {}, True)
                except:
                    print("Error: too many file calls")
                continue
            elif inp == "clear":
                if os == "Windows":
                    system('cls')
                else:
                    system("clear")
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
            elif inp == "endif":
                continue
            try:
                print((eval(Variables.filterVars(inp, vars, False))) if inp not in vars else print(1/0))
            except:
                print("Error: invalid operation") 