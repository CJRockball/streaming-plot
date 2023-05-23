import sqlite3
import time
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd


def update_data():
    
    connection = sqlite3.connect("stock.db")
    cursor = connection.cursor()
    
    data = cursor.execute(
        f"SELECT * FROM trades ORDER BY time DESC LIMIT 20").fetchall()
    connection.close
    
    df = pd.DataFrame(data, columns=['date', 'value'])
    df.sort_values(by='date', inplace=True)
    df['date'] = pd.to_datetime(df['date'],unit='s')
    df['ma15'] = df['value'].rolling(15).mean()   
    
    current_price = df.iloc[-1,1] #data[0][1]
    last_trade = df.iloc[-1,0] #time.ctime(data[0][0])
    ma15 = df.iloc[-1, 2]
    
    return last_trade, current_price, ma15
  
x_vals = []
y2_vals = []
y_vals = []
fig = plt.figure(figsize=(14,7))


def update_graph(i):
    last_trade, current_price, ma15 = update_data()
    
    if len(x_vals) < 50:
        x_vals.append(last_trade)
        #print(x_vals)
        y2_vals.append(ma15)
        y_vals.append(current_price)
    else:
        x_vals.append(last_trade)
        del x_vals[0]
        y2_vals.append(ma15)
        del y2_vals[0]
        y_vals.append(current_price)
        del y_vals[0]
        
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
    