#! /bin/python3


import numpy as np
import pandas as pd


def compute_cumulative_death_rate(csv_file_path, location_name):
    
    """
    Input: raw data from JHU, location name(country name or city name)

    Output: pandas.dataframe with columns
        1. cumulative death rate: #death / population. 
            If the location is a city, then city population.
        2. log of cumulative death rate
        3. area: country name or city name
    """
    pass
    return "dateframe with columns mentioned above"


def compute_std(df, column_name):
    """
    Compute the standard devirate 
    """
    return np.std(df["column_name"])