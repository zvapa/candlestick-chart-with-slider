## Creating candlestick charts with range slider using bokeh

<img src="./images/demo.gif" height=300>

This code snippet simulates parts of the workflow used in technical analysis:
* connecting to a sql database to extract price data for a specific trading instrument, and
* plotting a candlestick chart with a range slider and a tooltip for detailed price info

For illustration, I'm using daily OHLC price data for two instruments (EURUSD currency pair, and Apple stock) stored in a sqlite database, where each instrument represents a table. The script can easily be adopted to plot from csv files, assuming they contain the columns `date`, `open`, `high`, `low` & `close`.

### Usage:
Required dependencies:
* `bokeh`
* `pandas`

To use with `pipenv`, run: 
* `pip install pipenv` to install `pipenv`
* `pipenv install` to install dependencies
* `bokeh serve --show plotting.py` to open in browser

### Disclaimer:
This project is for education purpose and does not represent financial advice, nor should it be used in trading applications.
