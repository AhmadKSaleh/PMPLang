import matplotlib.pyplot as plt
from numpy import *
from variables import Variables

class Plot:
    def veval(x, vars, isFunc):
        return eval(Variables.filterVars(x, vars, isFunc))

    def plot3d(resolution, string, vars):
        # https://www.geeksforgeeks.org/three-dimensional-plotting-in-python-using-matplotlib/
        # tbh geeksforgeeks is the best python learning resource
        # - @AhmadKSaleh

        # defining surface and axes
        x = outer(linspace(-resolution, resolution, 30), ones(30))
        y = x.copy().T
        z = string.replace("x", f"outer(linspace(-{resolution}, {resolution}, 30), ones(30))")
        z = z.replace("y", f"outer(linspace(-{resolution}, {resolution}, 30), ones(30)).copy().T")
        z = Plot.veval(z, vars, True)

        fig = plt.figure()
        
        # syntax for 3-D plotting
        ax = plt.axes(projection ='3d')
        
        # syntax for plotting
        ax.plot_surface(x, y, z, cmap ='viridis', edgecolor ='green')
        ax.set_title('Surface plot geeks for geeks')
        plt.show()

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