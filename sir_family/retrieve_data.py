import pandas as pd
import numpy as np


"""
Process data from JHU

"""



fold_path = "D:/python_code/COVID-19/csse_covid_19_data/csse_covid_19_time_series"

confirm_global = pd.read_csv(fold_path + "/time_series_covid19_confirmed_global.csv")
confirm_us = pd.read_csv(fold_path + "/time_series_covid19_confirmed_US.csv" )

death_global = pd.read_csv(fold_path + "/time_series_covid19_deaths_global.csv")
death_us = pd.read_csv(fold_path + "/time_series_covid19_deaths_US.csv" )


remove_list = ["Country/Region", "Lat", "Long"]

confirm_global_cols = confirm_global.columns
confirm_global_wanted_cols = [col for col in confirm_global_cols if col not in remove_list]


UK_confirm = confirm_global.loc[confirm_global["Country/Region"] == "United Kingdom",
                                confirm_global_wanted_cols]
UK_confirm = np.sum(UK_confirm)
UK_confirm = UK_confirm[UK_confirm > 0]
UK_confirm_df = pd.DataFrame(UK_confirm, columns=["cases_count"])
#UK_confirm.keys
# UK_confirm = UK_confirm.loc[UK_confirm]

print(UK_confirm_df)