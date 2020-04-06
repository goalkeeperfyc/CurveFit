#! /bin/python3


import numpy as np
import pandas as pd
import datetime 


def compute_cumulative_death_rate(csv_file_path, location_name, state=False):
    
    """
    Input: 
        1. raw data from JHU
        2. location name (country level and state level)
        3. state, default False, 
            If we use state level data, then set state = True 

    Output: pandas.dataframe with columns
        1. cumulative death rate: #death / population. 
            If the location is a city, then city population.
        2. log of cumulative death rate
        3. area: country name or city name
    """
    # wanted columns
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday_str = datetime.datetime.strftime()
    date_range = pd.date_range("1/22/20", str(yesterday)[:10])
    date_range = [str(date).replace(" ", "").replace("\n", "") 
                  for date in date_range]
    df = pd.read_csv(csv_file_path)
    if state:
        df = df.rename(columns={"Province_State": "location_name"})
        df = df.groupby("location_name", as_index=False).sum()
        print(df.shape)
    else:
        df = df.rename(columns={"Country/Region": "location_name"})
    df = df.loc[df["location_name"] == location_name, ]
    print(df)
    new_df = df[date_range].T
    print(new_df)
    
    # df = pd.read_csv(csv_file_path)
    # if state:
        # df = df.groupby



    return "dateframe with columns mentioned above"


def compute_std(df, column_name):
    """
    Compute the standard devirate 
    """
    return np.std(df["column_name"])

compute_cumulative_death_rate(
    csv_file_path="D:/python_code/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv", 
    location_name="California", 
    state=True
)
