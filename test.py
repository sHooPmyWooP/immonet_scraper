import json
import pandas as pd
import numpy as np

with open("attr_dump.json","r") as f:
    data_json = json.load(f)

max_len = max([len(v) for k,v in data_json.items()])

for item in data_json.keys():
    val_array = data_json.get(item)
    if len(val_array)<max_len:
        print(item)
        for _ in range(max_len-len(val_array)):
            val_array.append(None)

df = pd.DataFrame.from_dict(data_json)

print(data_json)
print("asd")

# for key in list(attrs.keys()):
#     total_attrs.add(key)
#     try:
#         total_attrs_values[key] += [attrs.get(key)]
#     except KeyError:
#         total_attrs_values[key] = []
#         total_attrs_values[key] += [attrs.get(key)]
#
# print("attrs:", total_attrs)
# print("vals:", total_attrs_values)
# # df = pd.DataFrame.from_dict(total_attrs_values)
# # df_all_attributes.append(df)
# sleep(sleep_time)
#
# with open('attr_dump.json', 'w', encoding='utf-8') as f:
#     json.dump(total_attrs_values, indent=4, fp=f)
