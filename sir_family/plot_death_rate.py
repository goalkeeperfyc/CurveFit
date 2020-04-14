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


def compute_death_rate(data_file):
    df = pd.read_csv(os.getcwd() + "/data/" + data_file +".csv")
    df = df.loc[df["confirm_count"] >= 100, ]
    df["death_rate"] = df["death_count"] / df["confirm_count"]
    return df["death_rate"].values


country_list = ["United Kingdom", "France", "Italy", "Spain", 
                "Korea, South", "California", "New York",
                "New Jersey", "Florida", "Washington"]


fig, ax = plt.subplots(nrows=2, figsize=(20, 20))
for i in range(5):
    ax[0].plot(process_data(country_list[i], "confirm_count"), label=country_list[i])  
    ax[0].legend()
for i in range(5, 10):
    ax[1].plot(process_data(country_list[i], "confirm_count"), label=country_list[i]) 
    ax[1].legend()


fig, ax = plt.subplots(nrows=2, figsize=(20, 20))
for i in range(5):
    ax[0].plot(process_data(country_list[i], "death_count"), label=country_list[i])  
    ax[0].legend()
for i in range(5, 10):
    ax[1].plot(process_data(country_list[i], "death_count"), label=country_list[i]) 
    ax[1].legend()


fig, ax = plt.subplots(nrows=2, figsize=(20, 20))
for i in range(5):
    ax[0].plot(compute_death_rate(country_list[i]), label=country_list[i])  
    ax[0].legend()
for i in range(5, 10):
    ax[1].plot(compute_death_rate(country_list[i]), label=country_list[i]) 
    ax[1].legend()
