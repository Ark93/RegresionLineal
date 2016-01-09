import numpy as np
import matplotlib.pyplot as plt
import funciones as func
# function to elevate data to 10^3 in cientific notation
# because the data is originaly between 0 and 1
def sine3(x):
    return np.sin(x*(10**3))

#function to plot data
def plot_data(data):
    plt.plot(data[0],data[1],'ro')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Regresion Lineal Polinomial')
    plt.show()

def plot_prediction(data,prediction, rss):
    plt.plot(data[0],data [1], 'ro', data[0], prediction)
    plt.xlabel('x')
    plt.ylabel('y')
    textRSS = "RSS =", rss

    plt.title('Regresion Lineal Polinomial')
    plt.annotate( textRSS ,xy = (data[0].mean(), data[1].mean() ), xytext=(data[0].mean()-100, data[1].mean()+40))
    plt.show()


#function to get coefficient w1
def getW1(data):
    return ( ((data[0] - data[0].mean()) * (data[1] - data[1].mean())  ).sum() / ((data[0] - data[0].mean())**2).sum() )

#funciton to get coefficient w0
def getW0(data,w1):
    return data[1].mean() - (w1*data[0].mean())

#function to predict values of linear regression
def predict(feature,w):
    y = np.zeros(len(feature))
    for i in range(0,len(y)):
        y[i] = w[0] + w[1]*feature[i]
    return y


# # creation of 30 points of data, with x and y values
# data = np.random.rand(2,50)
# w = np.zeros(2)
# #data to 10^3
# data= e3(data)
#
# #caption of coefficients
# w[1] = getW1(data)
# w[0] = getW0(data,w[1])
#
# print w

y = predict(data[0],w)

rss = func.getRSS(data[1],y)
plot_prediction(data,y, rss)

