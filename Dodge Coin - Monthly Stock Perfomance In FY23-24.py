# %%
import yfinance as yf
import pandas as pd
#Fetch historical data 
crypto = 'DOGE-AUD'
data = yf.download(crypto, start='2023-01-01', end='2024-12-01')
data.reset_index(inplace=True)
print(data.head())

# %%
data = data[['Date', 'Adj Close']]
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
print(data.head())

# %%
# Calculate daily returns
data['Daily Return'] = data['Adj Close'].pct_change()

# Calculate monthly returns
data['Monthly Return'] = data.groupby([data['Year'], data['Month']])['Adj Close'].transform(lambda x: x.pct_change().sum())

# Group data by year and month for analysis
monthly_data = data.groupby([data['Year'], data['Month']])['Monthly Return'].agg(['mean', 'std']).reset_index()
monthly_data.columns = ['Year', 'Month', 'Avg Monthly Return', 'Monthly Volatility']
print(monthly_data.head())

# %%
import matplotlib.pyplot as plt

# Plot average monthly returns
plt.figure(figsize=(10, 6))
plt.bar(monthly_data['Month'], monthly_data['Avg Monthly Return'], color='blue')
plt.title('Dogecoin Average Monthly Returns')
plt.xlabel('Month')
plt.ylabel('Return')
plt.show()

# Plot monthly volatility
plt.figure(figsize=(10, 6))
plt.bar(monthly_data['Month'], monthly_data['Monthly Volatility'], color='orange')
plt.title('Dogecoin Monthly Volatility')
plt.xlabel('Month')
plt.ylabel('Volatility')
plt.show()



# %%
