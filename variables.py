import platform

class Variables:
    def filterVars(string, vars, isFunc):
        newStr = string
        try:
            if vars == {}:
                return string
            for var in vars.keys():
                if isFunc:
                    if var == "x" or var == "y":
                        continue
                    newStr = newStr.replace(var, str(vars[var][0]))
                else:
                    newStr = newStr.replace(var, str(vars[var][0]))
            return newStr
        except:
            return "1/0"

# vars = {"nameOfVar" : ["data", "VarType"]}
# for var in vars.keys() -> var = "nameOfVar"
# vars["nameOfVar"] => ["data", "VarType"]