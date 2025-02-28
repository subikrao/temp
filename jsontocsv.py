# import pandas as pd
# from pathlib import Path
# import json

# # set path to file
# p = Path(r'C:\Users\raos19\Documents\pocs\new.json')
# # read json
# with p.open('r', encoding='utf-8') as f:
#     data = json.loads(f.read())

# # create dataframe
# df = pd.json_normalize(data)

# # dataframe view
# #  pk            model  fields.codename           fields.name  fields.content_type
# #  22  auth.permission     add_logentry     Can add log entry                    8
# #  23  auth.permission  change_logentry  Can change log entry                    8
# #  24  auth.permission  delete_logentry  Can delete log entry                    8
# #   4  auth.permission        add_group         Can add group                    2
# #  10  auth.permission      add_message       Can add message                    4

# print(df.head())

# # save to csv
# df.to_csv('test.csv', index=False, encoding='utf-8')


import pandas as pd

# Read JSON file
df = pd.read_json('new.json')
# Convert to CSV
df.to_csv('output.csv', index=False)