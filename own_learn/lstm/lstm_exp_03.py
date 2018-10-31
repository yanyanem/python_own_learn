

import numpy
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

numpy.random.seed(2017)

def read_dataset():
	# load the dataset
	filename = 'data/us-air-carrier-traffic-statistic.csv'
	#filename = 'data/testlinear2.csv'
	#filename = 'data/testlinear.csv'
	#filename = 'data/AirPassengers.csv'
	dataframe = read_csv(filename, usecols=[1], engine='python', skipfooter=3)
	
	#filename = 'data_pk/ds_PACASABAT_110m-01.csv'
	#filename = 'data_pk/ds_U94911_83m-01.csv'
	#filename = 'data_pk/ds_94925_61m-01.csv'
	#filename = 'data_pk/ds_HUGEDB_45m-01.csv'
	#dataframe = read_csv(filename, usecols=[1], engine='python', skipfooter=3)
	
	#filename='data_pk/AirPassengers.csv'
	#dataframe = read_csv(filename, usecols=[2], engine='python', skipfooter=3)
	#filename='data_pk/AirPassengers3.csv'
	#dataframe = read_csv(filename, usecols=[1], engine='python', skipfooter=3)

	print('filename',filename)
	dataset = dataframe.values
	dataset = dataset.astype('float32')
	
	return dataset


# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):

	dataX, dataY = [], []
	for i in range(len(dataset)-look_back):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])

	return numpy.array(dataX), numpy.array(dataY)




def train_dataset(dataset,look_back=12,look_forward=6): 

	# normalize the dataset
	scaler = MinMaxScaler(feature_range=(0, 1))
	dataset = scaler.fit_transform(dataset)
	trainX, trainY = create_dataset(dataset, look_back)
	
	# reshape input to be [samples, time steps, features]
	trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
	
	# create and fit the LSTM network
	model = Sequential()
	model.add(LSTM(32, input_shape=(1, look_back)))
	model.add(Dense(8))
	model.add(Dense(1))
	model.compile(loss='mean_squared_error', optimizer='adam')
	model.summary()
	
	loss=1
	epochs=0
	loss_end=0.007
	epochs_end=100
	epochs_steps=5
	
	
	while (loss > loss_end and epochs < epochs_end):
		trainResult = model.fit(trainX, trainY, epochs=epochs_steps, batch_size=1, verbose=0)
		trainLoss = trainResult.history['loss']
		epochs=epochs+epochs_steps
		loss=trainLoss[-1]
		print('epochs',epochs,'loss',loss)
	
	# make predictions
	predict_start = numpy.array([numpy.append(trainX[-1][0],dataset[-1]).tolist()[1:]])
	#rolling forecast 
	testX_one = numpy.reshape(predict_start, (predict_start.shape[0], 1, predict_start.shape[1]))
	testPredict = []
	for i in range(0,look_forward):
		tp = model.predict(testX_one)
		testX_one=numpy.array([[numpy.append(testX_one,tp).tolist()[1:]]])
		testPredict.append(tp[0])
	
	testPredict = scaler.inverse_transform(testPredict)
	trainPredict = model.predict(trainX)
	# invert predictions
	trainPredict = scaler.inverse_transform(trainPredict)
	trainY = scaler.inverse_transform([trainY])
	trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
	print('Train Score: %.2f RMSE' % (trainScore))
	
	return trainPredict,testPredict

def plot_result(dataset,trainPredict,testPredict):
	dataset_X=[]
	dataset_Y=[]
	trainPredict_X=[]
	trainPredict_Y=[]
	testPredict_X=[]
	testPredict_Y=[]
	
	len0=len(dataset)
	len1=len(trainPredict)
	len2=len(testPredict)
	
	
	for i in range(0,len0+len2-1):

		if i<len0 :
			dataset_X.append(i)
			dataset_Y.append(dataset[i])
		if i>=(len0-len1) and i<len0 :
			trainPredict_X.append(i)
			trainPredict_Y.append(trainPredict[i-(len0-len1)])
		if i>=len0:
			testPredict_X.append(i)
			testPredict_Y.append(testPredict[i-len0])
			
	import matplotlib.pyplot as plt

	plt.plot(dataset_X,dataset_Y,color='black')
	plt.plot(trainPredict_X,trainPredict_Y,color='red')
	plt.plot(testPredict_X,testPredict_Y,color='blue')
	plt.show()


dataset = read_dataset()
look_back = 24
look_forward = 12
trainPredict,testPredict = train_dataset(dataset,look_back,look_forward)
print('testPredict',testPredict)

plot_result(dataset,trainPredict,testPredict)



