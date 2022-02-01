# PMPLang
Source Code for the Pythonic Mathmatical Programming Language (PMPLang)

# Installation
Make sure that you have python version `>3.10`
## Windows:
Use this command:
```batch
.\setup.bat
```
## Linux:
Use this command:
```shell
bash file.sh
```

# Commands:
| Commands     | Usage                                                                                                        | Example                    |
|--------------|--------------------------------------------------------------------------------------------------------------|----------------------------|
| `print`      | Prints either a specific string or a variable's value                                                        | `print Hello World!`       |
| `println`    | Same as `println`, but with a linebreak `\n` at the end                                                      | `println Hello World!`     |
| `jump`       | Jump to a specific line of code (starting at 1) if a certain condition is true (more info. in the help file) | `jump if x == 3 to line 4` |
| `function`   | Makes a function with a name (a mathmatical function, only use x and y as variables for the input)           | `function square = x**2`   | 
| `read`       | Executes a certain file                                                                                      | `read file.mpl`            |
| `clear`      | Clears the console                                                                                           | `clear`                    |
| `quit`       | Exits                                                                                                        | `quit`                     | 
| `input`      | Asks the user for a numerical input                                                                          | `input x`                  | 
| `inputASCII` | Asks the user for a single-character input converted to an ASCII value                                       | `inputASCII YesOrNo`       | 
| `sys`        | Executes a system command                                                                                    | `sys echo Hello!`          | 
| `display`    | Displays a function as a graph                                                                               | `display square`           |
| `display3d`  | Displays a function as a 3d graph                                                                            | `display3d sphere`         |
| `var`        | Adds a variable with a name (can only be an integer)                                                         | `var x = 3`                |                       
