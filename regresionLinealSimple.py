import numpy as np
import matplotlib.pyplot as plt

# function to elevate data to 10^3 in cientific notation
# because the data is originaly between 0 and 1
def e3(x):
    return x*(10**3)

#function to plot data
def plot_data(data):
    plt.plot(data[0],data[1],'ro')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Regresion Lineal Simple')
    plt.show()

# creation of 30 points of data, with x and y values
data = np.random.rand(2,30)

#data to 10^3
data= e3(data)

plot_data(data)
