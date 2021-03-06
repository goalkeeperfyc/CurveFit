import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def process_data(data_file):
    df = pd.read_csv(os.getcwd() + "/data/" + data_file)
    df = df.loc[df["confirm_count"] >= 100, ]
    return df["confirm_count"].values


def compute_alpha(population, case_array):
    daily_new_increasing = np.array([case_array[i + 1] - case_array[i] 
                                    for i in range(len(case_array) - 1)])
    population_array = np.array([population]) - case_array[: -1]
    alpha = daily_new_increasing / population_array
    return alpha



if __name__ == "__main__":
    country_dict = {
        "United Kingdom": 55980000,
        "France": 1386000000,
        "Italy": 60360000,
        "Spain": 46940000,
        "California": 39510000,
        "New York": 19540000,
        "New Jersey": 8882000,
        "Florida": 21300000,
        "Korea, South": 51470000,
        "Washington": 7615000
    }
    for key, value in country_dict.items():
    # case_array = process_data("UK.csv")
        case_array = process_data(key + ".csv")
        alpha = compute_alpha(value, case_array)
        alpha = alpha[alpha > 0]
        plt.plot(alpha, label=key)
        # p.set_label(key)
        plt.legend()
    # sns.jointplot(x=range(len(alpha)), y=alpha)
