# FREESTYLE PROJECT: Stock Market API with GUI

The following application provides the user with a GUI where he can input:
- A valid stock ticker
- A Start and End Date in the format ("YYYY-MM-DD")

The application then outputs:
- Price summary statistics for the given ticker
- The latest price of the date range

# DRIVERS

The two main drivers of this application are:
- The tkinter package: provides the user interface and the ability to simply customize it
- The pandas_datareader package: provides an interface to retrieve stock prices in pandas and to summarize the outputs
