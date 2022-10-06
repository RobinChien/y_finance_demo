#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


nflx_df = yf.download("NFLX", start='2020-01-01', end='2022-01-01')
nflx_df


# In[3]:


#Summary Stats for NFLX stocks
nflx_df.describe()


# In[4]:


# Historical view of the closing price of stock
plt.plot(nflx_df.index,
        nflx_df['Adj Close'])


# In[5]:


#Caculation of moving averages for 5 days of stocks
mas = [1, 5, 20, 60]
for ma in mas:
    column_name = "MA for {} days".format(str(ma))
    nflx_df[column_name] = nflx_df['Adj Close'].rolling(window=ma).mean()
nflx_df


# In[6]:


def compare_open_and_close_price(open_price, close_price):
    return 'red' if open_price > close_price else 'blue'

nflx_df['color'] = nflx_df.apply(lambda x: compare_open_and_close_price(x['Open'], x['Close']), axis=1)
nflx_df


# In[7]:


nflx_df = nflx_df.rename(columns = {'Adj Close' : 'MA for 1 days'})
nflx_df


# In[8]:


# Define the color by map
colors = {'red': '#ff207c', 'grey': '#42535b', 'blue': '#207cff', 'orange': '#ffa320', 'green': '#00ec8b'}


# In[13]:


mov_avg = {
            'MA (1)': {'Range':'1', 'Color': colors['blue'], 'linestyle': '-'},
            'MA (5)': {'Range':'5', 'Color': colors['red'], 'linestyle': '--'},
            'MA (20)': {'Range':'20', 'Color': colors['orange'], 'linestyle': '--'},
            'MA (60)': {'Range':'60', 'Color': colors['green'], 'linestyle': '--'}
}

date = nflx_df.index

for ma, ma_info in mov_avg.items():
    column_name = "MA for {} days".format(ma_info['Range'])
    plt.plot(date,
             nflx_df[column_name],
             color=ma_info['Color'],
             linestyle=ma_info['linestyle'],
             label=ma,
             linewidth=2
            )


# In[10]:


# Volumn bar plot
vol = nflx_df['Volume']

vol_plot = plt.bar(date, vol, width=4, color='darkgrey')
vol_plot

# Volumn bar plot
color = nflx_df['color']

vol_color_plot = plt.bar(date, vol, width=4, color=color)
vol_color_plot


# In[16]:


# Combine prices and volumes in one figure

# The setting of figure
plt.rc('figure', figsize=(15, 10))

# Create a figure and a set of subplots.
fig, axes = plt.subplots(
    3, # rows
    1, # columns
    gridspec_kw={'height_ratios': [3, 1, 1]} # Defines the relative heights of the rows
)

# Adjust the padding between and around subplots.
fig.tight_layout(pad=3)

# subplot 1
plot_close_price = axes[0]
for ma, ma_info in mov_avg.items():
    column_name = "MA for {} days".format(ma_info['Range'])
    plot_close_price.plot(date,
             nflx_df[column_name],
             color=ma_info['Color'],
             linestyle=ma_info['linestyle'],
             label=ma,
             linewidth=2
            )

# subplot 2
plot_vol = axes[1]
plot_vol.bar(date, vol, width=4, color='darkgrey')

# subplot 3
vol_color_plot = axes[2]
vol_color_plot.bar(date, vol, width=4, color=color)


# In[ ]:




