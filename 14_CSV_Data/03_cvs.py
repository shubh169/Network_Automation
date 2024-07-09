# Read CSV data in column format.

from csv import reader
from pprint import pprint

conf_dict={}
with open("02_config_in_column.csv") as csv_data:
    csv_content=reader(csv_data)
    ips=next(csv_content)

    for device in csv_content:
        for ip in ips:
            if not ip:
                continue
            if ip not in conf_dict.keys():
                conf_dict[ip]=list()

            n=ips.index(ip)
            if not device[n]:
                continue
            conf_dict[ip].append(device[n])


pprint(conf_dict)