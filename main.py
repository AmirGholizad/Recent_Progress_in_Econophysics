import MetaTrader5 as mt5
import numpy as np
import pandas as pd
import array
from matplotlib import pyplot as plt
import datetime
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
import pytz

def get_data(year,month,day):

    #connect to Metatrader 5
    mt5.initialize()
    # set time zone to UTC
    timezone = pytz.timezone("Etc/UTC")
    # create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
    utc_from = datetime.datetime(year, month, day, 9, 0, 0, tzinfo=timezone)
    utc_to = datetime.datetime(year, month, day, 12, 30, 0, tzinfo=timezone)
    # request AUDUSD ticks within 11.01.2020 - 11.01.2020
    ticks = mt5.copy_ticks_range("وتجارت", utc_from, utc_to, mt5.COPY_TICKS_ALL)

    if len(ticks)<1000:
        return []

    #print("Ticks received:", len(ticks))
    # create DataFrame out of the obtained data
    ticks_frame = pd.DataFrame(ticks)
    # convert time in seconds into the datetime format
    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')
    return ticks_frame


old_ticks = []
for j in range(3,5):
    new_ticks = get_data(2020,10,j)
    if len(new_ticks) == 0:
        continue
    elif len(old_ticks) == 0:
        old_ticks = new_ticks
    else:
        old_ticks = pd.concat([old_ticks,new_ticks])
tick_data = old_ticks.drop(old_ticks["last"] == 0).reset_index(drop=True)
print(tick_data)
