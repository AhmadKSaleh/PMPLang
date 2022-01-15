import matplotlib.pyplot as plt
from numpy import *
from variables import Variables

class Plot:
    def plot(resolution,y,vars):
        resolution = float(resolution)
        x = linspace(-resolution,resolution,100)
        y = Variables.filterVars(y, vars, True)
        # The above line has been added again to make functions update-able
        # - @AhmadKSaleh

        y = eval(y.replace("x", f"linspace(-{resolution},{resolution},100)"))
        # https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html

        # setting the axes at the centre
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # plot the function
        plt.plot(x,y, 'r')

        # show the plot
        plt.show()