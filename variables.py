import platform

class Variables:
    def filterVars(string, vars, isFunc):
        newStr = string
        try:
            if vars == {}:
                return string
            for var in vars:
                if isFunc:
                    if var == "x":
                        continue
                    newStr = newStr.replace(var, str(vars[var]))
                else:
                    newStr = newStr.replace(var, str(vars[var]))
            return newStr
        except:
            return "1/0"