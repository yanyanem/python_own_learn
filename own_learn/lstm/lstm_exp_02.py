
# http://blog.csdn.net/aliceyangxi1987/article/details/73420583

# env win tensorflow2 

import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
#%matplotlib inline

# fix random seed for reproducibility
numpy.random.seed(2017)



a=[[[1,2,3]]]
b=[4]
c=numpy.append(a,b)
c=c.tolist()
d=c[1:]
e=[[d]]

print('a',a)
print('b',b)
print('c',c)
print('d',d)
print('e',e)


def read_dataset():
	# load the dataset
	filename = 'data/us-air-carrier-traffic-statistic.csv'
	#filename = 'data/testlinear2.csv'
	#filename = 'data/testlinear.csv'
	#filename = 'data/AirPassengers.csv'
	dataframe = read_csv(filename, usecols=[1], engine='python', skipfooter=3)
	
	#filename='data_pk/data_sales_battery_monthly_PA1.csv'
	#dataframe = read_csv(filename, usecols=[3], engine='python', skipfooter=3)
	#dataframe = read_csv(filename, usecols=[5], engine='python', skipfooter=3)
	
	#filename = 'data_pk/ds_PACASABAT_110m-01.csv'
	#filename = 'data_pk/ds_U94911_83m-01.csv'
	#filename = 'data_pk/ds_94925_61m-01.csv'
	#filename = 'data_pk/ds_HUGEDB_45m-01.csv'
	#dataframe = read_csv(filename, usecols=[1], engine='python', skipfooter=3)
	
	#filename='data_pk/AirPassengers.csv'
	#dataframe = read_csv(filename, usecols=[2], engine='python', skipfooter=3)
	#filename='data_pk/AirPassengers3.csv'
	#dataframe = read_csv(filename, usecols=[1], engine='python', skipfooter=3)
	
	dataset = dataframe.values
	# 将整型变为float
	dataset = dataset.astype('float32')
	print('dataset',dataset)
	
	#plt.plot(dataset)
	#plt.show()
	
	return dataset


# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return numpy.array(dataX), numpy.array(dataY)


dataset = read_dataset()




# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

#print('scaler.fit_transform(dataset)',dataset)
#plt.plot(dataset)
#plt.show()

look_back = 12
# split into train and test sets
train_size = int(len(dataset) * 0.867)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size-look_back-1:len(dataset),:]

# use this function to prepare the train and test datasets for modeling
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)


print('trainX',trainX.shape)
print('trainY',trainY.shape)
print('testX',testX.shape)
print('testY',testY.shape)

# reshape input to be [samples, time steps, features]
trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

print('trainX',trainX.shape)
print('testX',testX.shape)


# create and fit the LSTM network
model = Sequential()
model.add(LSTM(32, input_shape=(1, look_back)))
model.add(Dense(8))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.summary()
model.fit(trainX, trainY, epochs=30, batch_size=1, verbose=1)



# make predictions
trainPredict = model.predict(trainX)
#testPredict = model.predict(testX)
#rolling forecast 
testX_one = numpy.reshape(testX[0], (testX[0].shape[0], 1, testX[0].shape[1]))
print('testX[0]',testX[0])
print('testX_one',testX_one)
testPredict = []
predict_size = len(testX)
for i in range(0,predict_size):
	#print('1:testX_one',testX_one)
	tp = model.predict(testX_one)
	#print('tp',tp)
	testX_one=numpy.append(testX_one,tp)
	#print('2:testX_one',testX_one)
	testX_one=testX_one.tolist()
	#print('3:testX_one',testX_one)
	testX_one=testX_one[1:]
	#print('4:testX_one',testX_one)
	testX_one=[[testX_one]]
	#print('5:testX_one',testX_one)
	testX_one=numpy.array(testX_one)
	#print('6:testX_one',testX_one)
	testPredict.append(tp[0])
	#print('testPredict',testPredict)

#for x in trainX: print ('trainX',x)
#for x in testX:  print ('testX',x)
#for x in trainPredict: print ('trainPredict',x)
#for x in testPredict: print ('testPredict',x)


# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])

print('trainPredict.shape',trainPredict.shape)
print('testPredict.shape',testPredict.shape)

trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))



# shift train predictions for plotting
trainPredictPlot = numpy.empty_like(dataset)
trainPredictPlot[:, :] = numpy.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict

print('look_back',look_back)
print('len(trainPredict)+look_back',len(trainPredict)+look_back)
print('len(trainPredict)',len(trainPredict))

# shift test predictions for plotting
testPredictPlot = numpy.empty_like(dataset)
testPredictPlot[:, :] = numpy.nan
testPredictPlot[len(trainPredict)+(look_back*1):len(dataset)-1, :] = testPredict

print('len(trainPredict)+(look_back*1)',len(trainPredict)+(look_back*1))
print('len(dataset)-1',len(dataset)-1)
print('len(testPredict)',len(testPredict))

# plot baseline and predictions
plt.plot(scaler.inverse_transform(dataset))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()







