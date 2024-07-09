import pandas as pd
from pprint import pprint

# Reading the CSV file into a DataFrame
df = pd.read_csv('01_config_in_row.csv', header=None)

# Creating the dictionary
conf_dict = {}
for index, row in df.iterrows():
    ip = row[0]
    if pd.isna(ip):
        continue
    conf_list = row[1:].dropna().tolist()
    conf_dict[ip] = conf_list

# Pretty print the dictionary
pprint(conf_dict)
