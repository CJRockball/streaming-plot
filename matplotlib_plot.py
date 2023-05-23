import sqlite3
import time
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd


def update_data():
    """
    Fetch new price from database
    """
    # Connect to sqlite db
    connection = sqlite3.connect("stock.db")
    cursor = connection.cursor()
    
    # Get 20 latest prices
    data = cursor.execute(
        f"SELECT * FROM trades ORDER BY time DESC LIMIT 20").fetchall()
    connection.close
    
    # Set data in a data frame 
    df = pd.DataFrame(data, columns=['date', 'value'])
    df.sort_values(by='date', inplace=True)
    df['date'] = pd.to_datetime(df['date'],unit='s')
    # Calculate moving average for the last 15 prices
    df['ma15'] = df['value'].rolling(15).mean()   
    
    # Get x(last_trade), y(current_price), moving average(ma15) to plot
    current_price = df.iloc[-1,1]
    last_trade = df.iloc[-1,0]
    ma15 = df.iloc[-1, 2]
    
    return last_trade, current_price, ma15
 
# Set up live plot 
x_vals = []
y2_vals = []
y_vals = []
fig = plt.figure(figsize=(14,7))


def update_graph(i):
    """
    Live plot of data
    """
    # Get new data
    last_trade, current_price, ma15 = update_data()
    
    # The plot will keep 50 data points in the graph
    if len(x_vals) < 50:
        # For the first 50 data point we can just add data
        x_vals.append(last_trade)
        y2_vals.append(ma15)
        y_vals.append(current_price)
    else:
        # Uppdate last data point and delete the oldest
        x_vals.append(last_trade)
        del x_vals[0]
        y2_vals.append(ma15)
        del y2_vals[0]
        y_vals.append(current_price)
        del y_vals[0]
    
    # plot graph 
    plt.cla()
    plt.plot(x_vals, y_vals, label='Price')
    plt.plot(x_vals, y2_vals, label='ma15')
    plt.grid()
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Simulated Price')
    plt.tight_layout()
    plt.xticks(rotation=45)
    

ani = FuncAnimation(fig, update_graph, interval=100) 
plt.show()  
  
  
    
# if __name__ == '__main__':
#     data = update_data()
#     print(time.ctime(data[0][0]), time.ctime(data[1][0]))
    