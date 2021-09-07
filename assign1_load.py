
#> Referencing https://www.postgresqltutorial.com/postgresql-python/connect/
import psycopg2
import csv


#. Set up connection parameters
conn = psycopg2.connect(
    host="acs-db.mlpolicylab.dssg.io",
    database="acs_data_loading",
    user="removed-for-git-hub",
    password="removed-for-git-hub")

#. Make a cursor that will temporarily save and then execute our script
cur = conn.cursor()

#> Save our table structure
# create_table = ("""
#     CREATE TABLE ewinter_acs_data (
#         index SERIAL PRIMARY KEY,
#         name VARCHAR NOT NULL,
#         pop_reporting_household VARCHAR NOT NULL,
#         married_house VARCHAR NOT NULL,
#         married_house_kids_under_18 VARCHAR NOT NULL,
#         married_house_nokids_under_18 VARCHAR NOT NULL,
#         female_no_spouse VARCHAR NOT NULL,
#         male_no_spouse VARCHAR NOT NULL,
#         state VARCHAR NOT NULL,
#         county VARCHAR NOT NULL,
#         tract VARCHAR NOT NULL,
#         block_group VARCHAR NOT NULL
#     )
# """)
# #. Make the table
# cur.execute(create_table)

#> Bring in the csv
#. Referenced: https://www.dataquest.io/blog/loading-data-into-postgres/

with open('transformed_block_groups_PA.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        #. Make the Insert command
        cur.execute("""
            INSERT INTO ewinter_acs_data
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, row)

#. Insert the data
conn.commit()

cur.close()
