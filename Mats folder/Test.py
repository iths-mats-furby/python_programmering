Test.py

import pandas as pd
import sqlite3

corona_vacc_df = pd.read_csv('data/vaccin_covid.csv')
db_connect = sqlite3.connect("corona_vacc.db")
cursor = db_connect.cursor()
corona_vacc_df.to_sql('corona_vacc', db_connect)
print(corona_vacc_df.head)
db_connect.commit()



