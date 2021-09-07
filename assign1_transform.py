
import pandas as pd

#> Bring in the dataset
household_df = pd.read_csv('block_groups_PA.csv')

#. Change the column headers. These will be dropped later, but we can
#. reference the change for guidance on table headers
household_df.drop(columns = '0', inplace= True)
household_df.rename(columns={'B11012_001E': 'pop_reporting_household'
                    , 'B11012_002E': 'married_house'
                    , 'B11012_003E': 'married_house_kids_under_18'
                    , 'B11012_004E': 'married_house_nokids_under_18'
                    , 'B11012_008E': 'female_no_spouse'
                    , 'B11012_013E': 'male_no_spouse'
                    }, inplace= True)
household_df.index.name = 'Index'

print(household_df.dtypes)

household_df.to_csv('transformed_block_groups_PA.csv', header=False)
