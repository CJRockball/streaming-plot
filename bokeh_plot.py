from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.driving import linear
import sqlite3
import time
import pandas as pd

p = figure(plot_width=1200, plot_height=400)
# Allow for following new data
p.x_range.follow = 'end'
p.x_range.follow_interval = 50
p.x_range.range_padding = 0
# Set date format for x axis
line1 = p.line([],[], color='firebrick', line_width=3)
ds1 = line1.data_source

@linear()
def update(i):
    connection = sqlite3.connect("stock.db")
    cursor = connection.cursor()
    
    data = cursor.execute(
        f"SELECT * FROM trades ORDER BY time DESC LIMIT 20").fetchall()
    connection.close
    
    df = pd.DataFrame(data, columns=['date', 'value'])
    df.sort_values(by='date', inplace=True)
    df['date'] = pd.to_datetime(df['date'],unit='s').dt.time
   
    
    current_price = df.iloc[-1,1]
    last_trade = data[0][0]

    ds1.data['x'].append(last_trade)
    ds1.data['y'].append(current_price)
    ds1.trigger('data', ds1.data, ds1.data)

curdoc().add_root(p)
curdoc().add_periodic_callback(update, 500)


