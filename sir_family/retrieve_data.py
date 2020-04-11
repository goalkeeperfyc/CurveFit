import pandas as pd
import numpy as np

"""
Process data from JHU

"""

fold_path = ("D:/python_code/COVID-19/csse_covid_19_data"
             "/csse_covid_19_time_series")

confirm_global = pd.read_csv(fold_path 
                             + "/time_series_covid19_confirmed_global.csv")
confirm_us = pd.read_csv(fold_path 
                         + "/time_series_covid19_confirmed_US.csv" )

death_global = pd.read_csv(fold_path 
                           + "/time_series_covid19_deaths_global.csv")
death_us = pd.read_csv(fold_path
                       + "/time_series_covid19_deaths_US.csv" )

output_path = "D:/python_code/CurveFit/sir_family/data/"


def country_level(
    country, 
    confirm_global=confirm_global, 
    death_global=death_global
    ):
    remove_list = ["Country/Region", "Lat", "Long"]
    global_cols = confirm_global.columns
    global_wanted_cols = [col for col in global_cols if col not in remove_list]

    confirm = confirm_global.loc[confirm_global["Country/Region"] == country,
                                 global_wanted_cols]
    confirm = np.sum(confirm)
    confirm = confirm[confirm > 0]
    result_df = pd.DataFrame(confirm, columns=["confirm_count"])

    death = death_global.loc[death_global["Country/Region"] == country,
                             global_wanted_cols]
    death = np.sum(death)
    result_df["death_count"] = death
    result_df.to_csv(output_path + country + ".csv")
    return result_df


def state_level(
    state, 
    confirm_global=confirm_global, 
    death_global=death_global
    ):
    remove_list = [
        "UID", "iso2", "iso3", "code3", "FIPS", "Admin2", "Province_State",
        "Country_Region", "Lat", "Long_", "Combined_Key"
    ]
    us_cols = confirm_us.columns
    us_wanted_cols = [col for col in us_cols if col not in remove_list]

    confirm = confirm_us.loc[confirm_us["Province_State"] == state,
                             us_wanted_cols]
    confirm = np.sum(confirm)
    confirm = confirm[confirm > 0]
    result_df = pd.DataFrame(confirm, columns=["confirm_count"])

    death = death_us.loc[death_us["Province_State"] == state,
                         us_wanted_cols]
    death = np.sum(death)
    result_df["death_count"] = death
    result_df.to_csv(output_path + state + ".csv")
    return result_df


country_level("United Kingdom")
country_level("Italy")
country_level("Spain")
country_level("Korea, South")
country_level("France")

state_level("California")
state_level("Florida")
state_level("New Jersey")
state_level("New York")
state_level("Washington")