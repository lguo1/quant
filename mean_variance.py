import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# get adjusted closing prices of 5 selected companies with Quandl
quandl.ApiConfig.api_key = 'byC6Gdt4zfRyj6yMUnYC'
selected = ['AAPL', 'BAC', 'VGK', 'C', 'GM', 'BX', 'FB']
data = quandl.get_table('WIKI/PRICES', ticker = selected,
                        qopts = { 'columns': ['date', 'ticker', 'adj_close'] },
date = { 'gte': '2014-1-1', 'lte': '2016-12-31' }, paginate=True)
