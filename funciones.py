def getRSS(data,prediction):
    rss = 0
    for i in range(0,len(data)):
        rss += (data[i] - prediction[i])**2
    return rss

def predict(feature,w):
    y = np.zeros(len(feature))
    for i in range(0,len(y)):
        y[i] = w[0] + w[1]*feature[i]
    return y