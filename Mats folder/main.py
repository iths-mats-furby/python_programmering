import pandas as pd
import sqlite3
from Test1 import databashantering
#from test 
#from pathlib import Path

def main():
    db = databashantering()
    #df = pd.read_csv('vaccin_covid.csv') #seed_database()
    #self.df = pd.read_csv('vaccin_covid.csv')
    db.table_create_and_insert() #create_database (tab_name, groupselect_table1, AVGselect_table2))
    # tab_name, groupselect_table1, AVGselect_table2
    db.seed_database()
    #db = ("vaccin_covid.csv")  #databashantering = sqlite3.connect("corona_vacc.db") # ("corona_vacc.db")
    #db = databashantering # ("corona_vacc.db")
    
    print("Hello main!") # Will be printed
    #db.create.database()
    #vax.col()b
#corona_vacc_df.head()
if __name__ == "__main__":
    main() # Call on the main function

