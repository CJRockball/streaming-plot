# Plot Streaming Websockets Data

Some small programs to try out streaming data with websockets. 
- <code style="color : Blue">fake_data.py</code> will generate a stock price and send it by websockets.
- ```save2sql.py``` will read the data on websockets and save it to a database.
- ```matplotlib_plot.py``` and ```bokeh_plot.py``` will read from the db and plot the data 'live'




## How to use

- Download repo
- You need three different servers, so run in three different terminals.
- run the fake_data from terminal ```python fake_data.py```
- run save2sql in it's own terminal ```python save2sql.py```
- run matplotlib_plot in it's own terminal ```python matplotlib_plot.py```
- OR run the bokeh server ```bokeh server --shoq bokeh_plot.py```
