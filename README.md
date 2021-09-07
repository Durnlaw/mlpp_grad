# mlpp_grad
I choose to focus my dataset on the households of Pennsylvania and break the data down based on marriage and children.

## Get Data: 
I opt to use a manual request as I can customize the call as I see fit. Libraries, although convenient, can receive bad updates and require documentation browsing. Customized requests are much faster for this purpose. 

The dataset specifically pulls: 
- The unique name of the row
- The reporting population in the block group/tract 
- The number of married households
- The number of married households with kids under 18 years old
- The number of married households without kids under 18 years old
- The number of households with only one female adult
- The number of households with only one male adult
- State (by number)
- County (by number)
- Tract (by number)
- Block Group (by number) 

Using the requests library, I retrieve the block group level data for PA households. To munge this data, I process it as a json, then transform it to a dataframe, and finally push as a csv.

## Transform/Prep
This step is the least impactful as the dataset comes mostly as integers. 

The one text-based column is long and unwieldy, although very descriptive. For this reason, I choose to leave it. I add a specific index for later use as a Primary Key

All unwieldy columns are renamed for reference purposes, and then later dropped to avoid insertting the column titles as a row in PSQL.

## Load

I choose to utilize the psycopg2 library as I already have some familiarity with it. 

After establishing the connection (user and pw removed), I create a cursor to execute the scripts. 

Next I create the ewinter_acs_table and insert the ~10 thousand rows into it using a for loop. In retrospect, there were more efficient ways of handling this task, but this does the trick for now.


## Overall
I am pleased with the API portion of this project and in the future would combine parts 1 and 2. 
In the future I am considering writing the database sections as functions to give more flexibility.
