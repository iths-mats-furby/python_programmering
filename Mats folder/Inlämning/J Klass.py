#from ipaddress import collapse_addresses
#from optparse import Values
import sqlite3
import pandas as pd
#import matplotlib.pyplot as pit
from pathlib import Path

class SqlDatabaseConn():

        def read_csv(self):
            self.df = pd.read_csv('vaccin-covid.csv')
            #self.df = pd.read_csv('\python_programmering\Mats folder\Inlämning\vaccin_covid.csv')
            print("read_csv is working")

class CleanData(SqlDatabaseConn):
        def __init__(self, column_name):
            self.column_name = column_name
        
        #"Replace Nan with 0"
        def replace_Nan(self):
            self.df = self.df.fillna(0, inplace=True)
            print("fillna is working")
        #Ersätter NA-värden med 0

        def clean_data(self):
            self.df = self
            #self.remove_blancs 
            trim_strings = lambda x: x.strip() if isinstance(x, str) else x
            return self.df.applymap(trim_strings)
        #Tar bort mellanslag

        def split_columns(self):
            self.df[{self.column_name}] = self.pd[{self.column_name}].str.split(',', extend = True)

        def sep_rows(self):
            self.df = self.df.explode("vaccine").reset_index(drop=True)
        
        def drop_duplicates(self):
            self.df.drop_duplicates()
    
class CoronaTables(CleanData, SqlDatabaseConn):
        def __init__(self, table_name, col, values):
        self.table_name = table_name
        self.col = col
        self.values = values

        def create_tables(self):
            db_con = sqlite3.connect('vaccin_covid.db') #Skapa en sql databas
            cursor = db_con.cursor()
            cursor.execute(f"CREATE TABLE {self.table_name} (id INTEGER PRIMARY KEY, {self.col}, TEXT)")
            db_con.commit()

        def insert_to_tables(self):
            db_con = sqlite3.connect('vaccin_covid.db') #Skapa en sql databas
            cursor = db_con.cursor() 
            cursor.execute(f"INSERT INTO {self.table_name} VALUES{self.values}, {self.df}")
            db_con.commit()

def main():
    handler = CoronaTables("vaccines", "vaccine", "?")
    handler.insert_to_tables()
    handler_clean_data = CleanData("vaccines")
    handler_clean_data.replace_Nan()

if __name__ == "__main__":
    main()


        




