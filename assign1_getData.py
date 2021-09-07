
import requests
#> Build out the URL and Request the data
#. Referenced: https://www.youtube.com/watch?v=l47HptzM7ao&ab_channel=DataCamp

#. Build the URL
HOST = 'https://api.census.gov/data'
yr = '2019'
dataset = 'acs/acs5?'
base_url = '/'.join([HOST, yr, dataset])

#. Add additional sections
get = 'get=NAME,B11012_001E,B11012_002E,B11012_003E,B11012_004E,B11012_008E,B11012_013E'
#. Total Pop Reporting Household, Married House, Married with kids under 18,
#. Married with no kids under 18, Female no Spouse, Male no Spouse
block_state = '&for=block%20group:*&in=state:42&in=county:*&in=tract:*'
cmbnd = ''.join([base_url, get, block_state])
print(cmbnd)

r = requests.get(cmbnd)

#. For reference if need be
#// 'https://api.census.gov/data/2019/acs/acs5?get=NAME,B01001_001E&for=block%20group:*&in=state:42&in=county:*&in=tract:*'


#> Move to json, then a csv
import csv
#. Referenced: https://www.codegrepper.com/code-examples/javascript/requests+json+response+list+data+python

import json
json_data = json.loads(r.text)
# print(type(json_data))

import pandas as pd
text_df = pd.DataFrame(json_data)
# print(text_df)

text_df.to_csv('block_groups_PA.csv', header = False)

#! Done! 