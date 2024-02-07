import random

import pandas as pd
import numpy as np



def generate_working_hour_means(df):
    country_codes_list = df.company_location.unique() 
    distribution_mean = {}
    for country in country_codes_list:
        distribution_mean[country] = np.random.uniform(30, 50)

    return distribution_mean


def generate_working_hours(df, distribution_mean:dict):
    for country_code, mean in distribution_mean.items():
        mask = df['company_location'] == country_code
        num_records = mask.sum()

        standard_dev = random.randint(1, 5)
        working_hours = np.random.normal(loc=mean, scale=standard_dev, size=num_records)
        df.loc[mask, "weekly_hours"] = working_hours

    return df


def main():
    df_salaries = pd.read_csv("ds_salaries.csv")
    distribution_mean = generate_working_hour_means(df_salaries)
    df_salaries = generate_working_hours(df_salaries, distribution_mean)
    #df_salaries.to_csv('path', index=False)

if __name__ == "__main__":
    main()