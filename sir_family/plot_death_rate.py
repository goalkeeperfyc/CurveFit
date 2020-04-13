# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:14:19 2020

@author: Yucheng Fang
Email: goalkeeperyucheng@gmail.com
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def process_data(data_file, column_name):
    df = pd.read_csv(os.getcwd() + "/data/" + data_file +".csv")
    df = df.loc[df[column_name] >= 100, ]
    return df[column_name].values



country_list = ["United Kingdom", "France", "Italy", "Spain", 
                "California", "New York", "New Jersey",
                "Florida", "Korea, South", "Washington"]


# confirm_count = process_data(country_list[0], "death_count")

fig, ax = plt.subplots(nrows=2, figsize=(20, 20))
for i in range(2):
    ax[i].plot(process_data(country_list[4 * i], "death_count"), label=country_list[4 * i])  # 4 * i is the 1st, 5th elements in country_list
    ax[i].plot(process_data(country_list[4 * i + 1], "death_count"), label=country_list[4 * i + 1])  # 4 * i + 1 is the 2nd, 6th elements in country_list
    ax[i].plot(process_data(country_list[4 * i + 2], "death_count"), label=country_list[4 * i + 2])  # 4 * i + 1 is the 3rd, 7th elements in country_list
    ax[i].plot(process_data(country_list[4 * i + 3], "death_count"), label=country_list[4 * i + 3])  # 4 * i + 1 is the 4th, 8th elements in country_list
    ax[i].legend()


fig2, ax2 = plt.subplots(nrows=2, figsize=(20, 20))
for i in range(2):
    ax2[i].plot(process_data(country_list[4 * i], "confirm_count"), label=country_list[4 * i])  # 4 * i is the 1st, 5th elements in country_list
    ax2[i].plot(process_data(country_list[4 * i + 1], "confirm_count"), label=country_list[4 * i + 1])  # 4 * i + 1 is the 2nd, 6th elements in country_list
    ax2[i].plot(process_data(country_list[4 * i + 2], "confirm_count"), label=country_list[4 * i + 2])  # 4 * i + 1 is the 3rd, 7th elements in country_list
    ax2[i].plot(process_data(country_list[4 * i + 3], "confirm_count"), label=country_list[4 * i + 3])  # 4 * i + 1 is the 4th, 8th elements in country_list
    ax2[i].legend()
# p.show()
