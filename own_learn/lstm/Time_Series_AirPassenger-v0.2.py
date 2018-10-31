
# coding: utf-8

# # Steps to Tackle a Time Series Problem (with Codes in Python)
# Note: These are just the codes from article

# ## Loading and Handling TS in Pandas

# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
get_ipython().magic('matplotlib inline')
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6


# In[14]:



#Note: aim is not to teach stock price forecasting. It's a very complex domain and I have almost no clue about it. Here I will demonstrate the various techniques which can be used for time-series forecasting

#csvFile = 'AirPassengers.csv'
csvFile = 'us-air-carrier-traffic-statistic.csv'

data = pd.read_csv(csvFile)


#print data.head()
#print '\n Data Types:'
#print data.dtypes


# In[15]:


dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
# dateparse('1962-01')
data = pd.read_csv(csvFile, parse_dates=['Month'], index_col='Month',date_parser=dateparse)

#print data.head()


# In[16]:


#check datatype of index
#data.index


# In[17]:


#convert to time series:
ts = data['#Passengers']
ts.head(10)


# ### Indexing TS arrays:

# In[18]:


#1. Specific the index as a string constant:
#ts['1949-01-01']


# In[19]:


#2. Import the datetime library and use 'datetime' function:
from datetime import datetime
#ts[datetime(1949,1,1)]


# #Get range:

# In[20]:


#1. Specify the entire range:
#ts['1949-01-01':'1949-05-01']


# In[21]:


#2. Use ':' if one of the indices is at ends:
#ts[:'1949-05-01']


# Note: ends included here

# In[22]:


#All rows of 1962:
#ts['1949']


# Reading as datetime format:

# # Checking for stationarity
# 
# ## Plot the time-series

# In[23]:


plt.plot(ts)


# ### Function for testing stationarity

# In[24]:


from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
    
    #Determing rolling statistics
    rolmean = pd.rolling_mean(timeseries, window=12)
    rolstd = pd.rolling_std(timeseries, window=12)

    #Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    
    #Perform Dickey-Fuller test:
    print 'Results of Dickey-Fuller Test:'
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print dfoutput


# In[25]:


test_stationarity(ts)


# # Making TS Stationary
# 
# 
# ## Estimating & Eliminating Trend
# 

# In[26]:


ts_log = np.log(ts)
plt.plot(ts_log)

ts_log.head(10)


# ## Smoothing:
# 
# ### Moving average

# In[27]:


moving_avg = pd.rolling_mean(ts_log,12)
plt.plot(ts_log)
plt.plot(moving_avg, color='red')
moving_avg.head(20)


# In[28]:


ts_log_moving_avg_diff = ts_log - moving_avg
ts_log_moving_avg_diff.head(15)


# In[29]:


ts_log_moving_avg_diff.dropna(inplace=True)
ts_log_moving_avg_diff.head()


# In[30]:


test_stationarity(ts_log_moving_avg_diff)


# ### Exponentially Weighted Moving Average

# In[31]:


expwighted_avg = pd.ewma(ts_log, halflife=12)
plt.plot(ts_log)
plt.plot(expwighted_avg, color='red')
# expwighted_avg.plot(style='k--')


# In[32]:


ts_log_ewma_diff = ts_log - expwighted_avg
test_stationarity(ts_log_ewma_diff)


# ## Eliminating Trend and Seasonality

# ### Differencing:

# In[33]:


#Take first difference:
ts_log_diff = ts_log - ts_log.shift()
plt.plot(ts_log_diff)
ts_log_diff.head(10)


# In[34]:


ts_log_diff.dropna(inplace=True)
test_stationarity(ts_log_diff)


# ### Decomposition:

# In[35]:


from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(ts_log)

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.subplot(411)
plt.plot(ts_log, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal,label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='best')
plt.tight_layout()


# In[36]:


ts_log_decompose = residual
ts_log_decompose.dropna(inplace=True)
test_stationarity(ts_log_decompose)


# # Final Forecasting

# In[37]:


from statsmodels.tsa.arima_model import ARIMA


# ### ACF & PACF Plots

# In[38]:


#ACF and PACF plots:
from statsmodels.tsa.stattools import acf, pacf  

lag_acf = acf(ts_log_diff, nlags=20)
lag_pacf = pacf(ts_log_diff, nlags=20, method='ols')

#Plot ACF:    
plt.subplot(121)    
plt.plot(lag_acf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
plt.title('Autocorrelation Function')

#Plot PACF:
plt.subplot(122)
plt.plot(lag_pacf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()


# ### AR Model:

# In[39]:


#MA model:
model = ARIMA(ts_log, order=(10, 1, 0))  
results_AR = model.fit(disp=-1)  
plt.subplot(121)  
plt.plot(ts_log_diff)
plt.plot(results_AR.fittedvalues, color='red')
plt.title('RSS: %.4f'% sum((results_AR.fittedvalues-ts_log_diff)**2))

predict_AR = results_AR.predict(start='2012-08-01',end='2013-08-01',typ='levels')

plt.subplot(122)  
plt.plot(ts_log)
plt.plot(predict_AR)




# ### MA Model

# In[40]:


model = ARIMA(ts_log, order=(0, 1, 2))  
results_MA = model.fit(disp=-1)  
plt.plot(ts_log_diff)
plt.plot(results_MA.fittedvalues, color='red')
plt.title('RSS: %.4f'% sum((results_MA.fittedvalues-ts_log_diff)**2))


# ### ARIMA Model:

# In[41]:


model = ARIMA(ts_log, order=(10, 1, 2))  
results_ARIMA = model.fit(disp=-1)  
plt.plot(ts_log_diff)
plt.plot(results_ARIMA.fittedvalues, color='red')
print len(results_ARIMA.fittedvalues)
print len(ts_log_diff)
print len(ts_log)
plt.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-ts_log_diff)**2))


# # Model Predict

# In[215]:



print(ts_log[0:5])
print(ts_log_diff[0:5])

scope_len=150
pos_start=30
pos_end=pos_start+scope_len

print pos_end 
print ts_log.index[pos_end] , ts_log[pos_end]

#predict_start='2012-08-01'
predict_start=ts_log.index[pos_end]
predict_end='2015-08-01'

print '\n predict_start, predict_end'
print predict_start, predict_end

ts_log_new = ts_log[pos_start:pos_end]
ts_log_diff_new = ts_log_diff[pos_start:pos_end-1]

#print '\n ts_log_new' ,ts_log_new
#print '\n ts_log_diff_new', ts_log_diff_new

plt.plot(ts_log)
plt.plot(ts_log_new)


# In[216]:


model = ARIMA(ts_log_new, order=(10, 1, 2))  
results_ARIMA = model.fit(disp=-1)  
print results_ARIMA.summary() 
plt.subplot(311)  
plt.plot(ts_log_diff_new)
plt.plot(results_ARIMA.fittedvalues, color='red')
plt.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-ts_log_diff_new)**2))

predict_ARIMA = results_ARIMA.predict(start=predict_start,end=predict_end,typ='levels')

plt.subplot(312)  
plt.plot(ts_log)
plt.plot(ts_log_new)
plt.plot(predict_ARIMA,color='red')

plt.subplot(313)  
plt.plot(ts)
plt.plot(np.exp(ts_log_new))
plt.plot(np.exp(predict_ARIMA),color='red')


# ### Convert to original scale:

# In[44]:


predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
print predictions_ARIMA_diff.head()


# In[45]:


predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
print predictions_ARIMA_diff_cumsum.head()


# In[46]:


predictions_ARIMA_log = pd.Series(ts_log.ix[0], index=ts_log.index)
predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum,fill_value=0)
predictions_ARIMA_log.head()


# In[47]:


plt.plot(ts_log)
plt.plot(predictions_ARIMA_log)


# In[48]:


predictions_ARIMA = np.exp(predictions_ARIMA_log)
plt.plot(ts)
plt.plot(predictions_ARIMA)
plt.title('RMSE: %.4f'% np.sqrt(sum((predictions_ARIMA-ts)**2)/len(ts)))


# In[50]:




