# price = 5.232425
#
# # so here 2f is for only 2 point from decimal
# print(f"hey price if {price:.2f}")
#
#
# # if we want to show curly braces in my f string so we use double curly braces
# print(f"hey ram pal {{name}}")

# import time
# a = time.time()
# print(a)
#
# time = time.strptime(%H)












import pandas as pd
import psycopg2

#establish connection to the postgresql database
connection_string = "postgresql://doadmin:AVNS_AZ-3Q1oUpp9WnsReBBX@devtradingsagedb-do-user-12481132-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require"
conn = psycopg2.connect(connection_string)

#define input dates
date1 = '2023-01-02'
date2 = '2023-01-05'

#query the database to select OI for each strike and instrument type for both input dates
query = f'''
SELECT DISTINCT strike, instrument_type, 
SUM(CASE WHEN date = '{date1}' THEN OI ELSE 0 END) as OI1, 
SUM(CASE WHEN date = '{date2}' THEN OI ELSE 0 END) as OI2 
FROM test_assignment 
WHERE date IN ('{date1}', '{date2}')
GROUP BY strike, instrument_typ
'''

df = pd.read_sql_query(query, conn)

#calculate difference in OI and add as a new column
df['OI_difference'] = df['oi2'] - df['oi1']

#pivot the dataframe to get the desired output format
output = df.pivot(index='strike', columns='instrument_type', values='OI_difference')

#rename columns
output.columns = [col + ' OI Difference' for col in output.columns]

print(output)
