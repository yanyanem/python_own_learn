
from __future__ import print_function

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import sequence
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Embedding
from keras.layers import LSTM, SimpleRNN, GRU
from keras.datasets import imdb
from keras.optimizers import RMSprop

from sklearn.preprocessing import MinMaxScaler

np.random.seed(2017)  # for reproducibility

def initData():

	train_df = pd.read_csv("data\\us-air-carrier-traffic-statistic.csv")
	
	print(train_df[:10])
	
	MonthList=train_df['Month']
	PassengerNumList=train_df['U.S. Air Carrier Traffic Statistics - Passenger Enplanements']
	
	MonthList_2 = [ m.replace('-','')for m in MonthList ]
	x=[ i for i in range(0,len(MonthList))]
	
	PassengerNum=[]
	print('p value')
	for p in PassengerNumList:
		PassengerNum.append(p)
	
	#plt.plot(x,PassengerNum)
	#plt.show()

	return MonthList, PassengerNum
	

def prepareData(PassengerNum,windows):

	print ('PassengerNum',PassengerNum)
	len_0 = len(PassengerNum)
	X=[]
	y=[]
	for i in range(0,len_0-windows):
		X.append( [[x] for x in PassengerNum[i:i+windows] ] )
		y.append( [ PassengerNum[i+windows] ] )


	X=np.array(X)
	y=np.array(y)
	print('X',X.shape)
	print('y',y.shape)
	
	#scaler = MinMaxScaler(feature_range=(0, 1))
	#y = scaler.fit_transform(y.reshape(-1, 1))
	#print ('y',y)
	
	return X,y
	
def prepareData2(ds,timestep=1, look_back=1, look_ahead=1):

	print ('ds',ds)
	len_ds = len(ds)
	print('len_ds',len_ds)
	X=[]
	y=[]
	for i in range(0,len_ds-look_back):
		X.append( [[x] for x in ds[i:i+look_back] ] )
		y.append( [ ds[i+look_back] ] )

	print('X',X)
	print('y',y)
	
	return X,y

def trainLSTM(X_data,y_data):

	print('prepare X_train , y_train, X_test, y_test')
	
	len_0 = len(X_data)
	pos = int(len_0*0.9)
	
	print('pos',pos)
	
	X_train = X_data[:pos]
	y_train = y_data[:pos]
	X_test = X_data[pos:]
	y_test = y_data[pos:]
	
	print('X_train.shape',X_train.shape)
	print('y_train.shape',y_train.shape)
	print('X_test.shape',X_test.shape)
	print('y_test.shape',y_test.shape)

	print('Build model...')
	hiddenSize=32
	size_input=len(X_train[0][0])
	print('size_input',size_input)
	model = Sequential()
	#model.add(LSTM(hiddenSize, input_shape=(None, size_input), return_sequences=True))
	model.add(LSTM(hiddenSize, input_shape=(None, size_input)))
	model.add(Dense(1))
	#model.add(Activation('relu'))
	model.add(Activation('tanh'))
	#model.add(Dropout(0.2))
	#model.add(Activation('linear'))
	#model.add(Activation('sigmoid'))
	#model.add(Activation('softmax'))
	#model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.01),metrics=['accuracy'])
	#model.compile(loss='mean_squared_error', optimizer='sgd')
	#model.compile(loss='mean_squared_error', optimizer='rmsprop')
	model.compile(loss='mean_squared_error', optimizer='adam')
	#model.compile(loss='mape', optimizer='adam')
	# try using different optimizers and different optimizer configs
	#model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
	model.summary()
	
	
	print('Train...')
	batch_size=10
	model.fit(X_train, y_train, batch_size=batch_size, epochs=15)

	#score, acc = model.evaluate(X_test, y_test, batch_size=batch_size)
	#print('Test score:', score)
	#print('Test accuracy:', acc)
	
	y_predict = model.predict(X_test,verbose=1)
	
	print('y_test',y_test)
	print('y_predict',y_predict)




MonthList, PassengerNum = initData()

#timestep=1
#look_back=6
#look_ahead=2
#X_data,y_data = prepareData2(PassengerNum,timestep,look_back,look_ahead)

windows=60
s=0
e=200
X_data,y_data = prepareData(PassengerNum[s:e],windows)


trainLSTM(X_data,y_data)




# use LSTM for forecasting
def create_dataset(dataset, timestep=1, look_back=1, look_ahead=1):
	
	ds = dataset.reshape(-1, 1)
	#print ('ds',ds)
	dataX = lagmat(dataset, maxlag=look_back, trim="both", original='ex')
	dataY = lagmat(dataset[look_back:], maxlag=look_ahead, trim="backward", original='ex')
	# reshape and remove redundent rows
	dataX = dataX.reshape(dataX.shape[0], timestep, dataX.shape[1])[:-(look_ahead-1)]
	return np.array(dataX), np.array(dataY[:-(look_ahead-1)])

def create_dataset2(dataset, timestep=1, look_back=1, look_ahead=1):

	print ('dataset',dataset)
	len_0 = len(PassengerNum)
	X=[]
	y=[]
	for i in range(0,len_0-windows):
		X.append( [[x] for x in PassengerNum[i:i+windows] ] )
		y.append( [ PassengerNum[i+windows] ] )

	print('X',X)
	print('y',y)
	
	return X,y


import keras.models as kModels
import keras.layers as kLayers
import warnings


from sklearn.metrics import mean_squared_error


def test(PassengerNum):

	PassengerNum = np.array(PassengerNum)
	cutoff=24
	train = PassengerNum[:-cutoff]
	test = PassengerNum[-cutoff:]

	scaler = MinMaxScaler(feature_range=(0, 1))
	
	print ('train',train)
	trainstd = scaler.fit_transform(train.reshape(-1, 1))
	print ('trainstd',trainstd)
	print ('test',test)
	teststd = scaler.transform(test.reshape(-1, 1))
	print ('teststd',teststd)
	lookback=60
	lookahead=24
	timestep=1
	trainX, trainY = create_dataset(trainstd, timestep=1, look_back=lookback, look_ahead=lookahead)

	# define LSTM model 
	batch_size=11
	model = kModels.Sequential()
	model.add(kLayers.LSTM(48, batch_size=batch_size, input_shape=(1, lookback), kernel_initializer='he_uniform'))
	model.add(kLayers.Dense(lookahead))
	model.compile(loss='mean_squared_error', optimizer='adam')
	model.fit(trainX, trainY, epochs=20, batch_size=batch_size, verbose=0)

	# visual 
	feedData = scaler.transform(PassengerNum[100:160].reshape(-1, 1)).copy()
	feedX = (feedData).reshape(1, 1, lookback)
	feedX = (feedX)
	prediction1 = model.predict(feedX)

	predictionRaw = scaler.inverse_transform(prediction1.reshape(-1, 1))
	actual1 = PassengerNum[160:180].copy().reshape(-1, 1)
	MAPE = (np.abs(predictionRaw-actual1)/actual1).mean()

	plt.plot(predictionRaw, label='Prediction')
	plt.plot(actual1, label='Actual')
	plt.title("MAPE = %.4f" % MAPE)
	plt.legend(loc='best')
	plt.xlim((0, 23))
	plt.xlabel("Month")
	plt.show()






#test(PassengerNum)

