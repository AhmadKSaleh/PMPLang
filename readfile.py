from os import system
from matplotlib.pyplot import contour
from variables import Variables
from plot import Plot

operators = ["sys", "var", "function", "read", "print", "println"]
operands = ["+", "-", "*", "/", "(", ")"]

class ReadFile:
    def handleJump(splits, vars):
        a = eval(Variables.filterVars(splits[2], vars, False))
        b = eval(Variables.filterVars(splits[4], vars, False))
        match splits[3]:
            case "==":
                return int(a == b)
            case "!=":
                return int(a != b)
            case ">=":
                return int(a >= b)
            case "<=":
                return int(a <= b)
            case ">":
                return int(a > b)
            case "<":
                return int(a < b)
        return 0
    def loop(vars, fileName, functions, os):
        # ! WE HAVE WAY TOO MANY VARIABLES
        # TODO: REDUCE VARIABLE COUNT
        lineCount = 0
        ended = False
        shouldJump = False
        file = open(fileName, 'r')
        lines = file.readlines()
        lines.insert(len(lines), "\n") # we have to do this madness to fix the jump problem
        lines = [line.replace("\n", "") if line != "\n" else "\n" for line in lines]
        line = lines[0]
        splits = line.split()
        cutlines = lines
        while not ended:
            if shouldJump:
                cutlines = lines[int(splits[7])-1:]
                shouldJump = False
            for lineCount in range(len(cutlines)):
                line = cutlines[lineCount]
                splits = line.split()
                if line == "\n":
                    continue
                elif splits[0] == "derivative":
                    if splits[2] == "->":
                        try:
                            functions[splits[3]] = [Plot.derivative(functions[splits[1]][0], vars), functions[splits[1]][1]]
                        except:
                            functions[splits[3]] = [Plot.derivative(functions[splits[1]][0], vars), 5]
                    else:
                        raise ZeroDivisionError
                    continue
                elif splits[0] == "//":
                    if splits[len(splits)-1] != "//":
                        raise ZeroDivisionError
                    continue
                elif splits[0] == "jump":
                    if splits[1] == "if" and splits[5] == "to" and splits[6] == "line":
                        if ReadFile.handleJump(splits, vars) == 1:
                            shouldJump = True
                            break
                    else:
                        raise ZeroDivisionError
                    continue
                elif splits[0] == "input":
                    vars[splits[1]] = int(input())
                    continue
                elif splits[0] == "inputASCII":
                    vars[splits[1]] = ord(input())
                    continue
                elif splits[0] == "print":
                    if line[6:] in vars:
                        print(vars[line[6:]], end="")
                    else:
                        print(line[6:], end="")
                    continue
                elif splits[0] == "println":
                    if line[8:] in vars:
                        print(vars[line[8:]])
                    else:
                        print(line[8:])
                    continue
                elif line == "quit":
                    ended = True
                    break
                elif splits[0] == "display":
                    Plot.plot(functions[splits[1]][1], Variables.filterVars(functions[splits[1]][0], vars, True), vars)
                    continue
                elif splits[0] == "display3d":
                    Plot.plot3d(functions[splits[1]][1], Variables.filterVars(functions[splits[1]][0], vars, True), vars)
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
                elif line == "clear":
                    if os == "Windows":
                        system('cls')
                    else:
                        system("clear")
                    continue
                elif splits[0] == "sys":
                    system(line[4:])
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
                    print((eval(Variables.filterVars(line, vars, False))) if line not in vars else print(1/0))
                except:
                    print("Error: invalid operation") 
            if lineCount == len(cutlines)-1 or line == "quit" and not shouldJump:
                ended = True