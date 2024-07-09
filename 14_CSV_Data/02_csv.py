
# Read CSV data in row format.

from csv import reader
from pprint import pprint

conf_dict={}
with open("01_config_in_row.csv") as csv_data:
    csv_content=reader(csv_data)
    for device in csv_content:
        ip=device[0]
        if not ip:
            continue

        final_conf=[]
        for conf in device[1:]:
            if not conf:
                continue
            final_conf.append(conf)

        conf_dict[ip]=final_conf


pprint(conf_dict)




