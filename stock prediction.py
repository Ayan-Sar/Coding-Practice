import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import math
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

prices=pd.read_csv('prices.csv')
prices.head()

ayan = prices[prices['symbol'] == 'YHOO']
ayan_prices = ayan.close.values.astype('float32')
ayan_prices = ayan_prices.reshape(1762,1)
ayan_prices.shape
plt.plot(ayan_prices)
plt.show()
np.random.seed(7)

scaler = MinMaxScaler(feature_range=(0,1))
ayan_prices=scaler.fit_transform(ayan_prices)
train_size = int(len(ayan_prices)*0.80)
test_size = len(ayan_prices) - train_size
train,test = ayan_prices[0:train_size,:],ayan_prices[train_size:len(ayan_prices),:]
print(len(train),len(test))
def create_dataset(dataset,look_back=1):
    dataX,dataY=[],[]
    for i in range(len(dataset) - look_back-1):
        a = dataset[i:(i + look_back),0]
        dataX.append(a)
        dataY.append(dataset[i+look_back,0])
    return np.array(dataX),np.array(dataY)
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))