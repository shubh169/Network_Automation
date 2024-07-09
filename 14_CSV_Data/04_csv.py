from csv import DictReader
from pprint import pprint


conf_dict={}
with open("02_config_in_column.csv") as csv_data:
    csv_content=DictReader(csv_data)
    ips=csv_content.fieldnames
    for row in csv_content:
        for ip in ips:
            if not ip:
                continue
            if ip not in conf_dict.keys():
                conf_dict[ip]=[]

            if not row[ip]:
                continue
            conf_dict[ip].append(row[ip])

pprint(conf_dict)



