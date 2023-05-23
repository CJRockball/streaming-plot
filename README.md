# Plot Streaming Websockets Data

Set up one server to generate fake data, read it to a sql database. The plotting functions read it from the db and plots it.

## How to use

- Download repo
- You need three different servers, so run in three different terminals.
- run the fake_data from terminal ```python fake_data.py```
- run save2sql in it's own terminal ```python save2sql.py```
- run matplotlib_plot in it's own terminal ```python matplotlib_plot.py```
- OR run the bokeh server ```bokeh server --shoq bokeh_plot.py```
