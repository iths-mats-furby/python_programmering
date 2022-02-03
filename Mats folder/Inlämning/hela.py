#from ipaddress import collapse_addresses
#from optparse import Values
import sqlite3
import pandas as pd
#import matplotlib.pyplot as pit
#from pathlib import Path

class SqlDatabas():
        def read_csv(self):
            self.df = pd.read_csv('vaccin-covid.csv')
            print("read_csv fungerar")

class Städadata(SqlDatabas):
        def __init__(self, column_name):
            self.column_name = column_name
        
        def replace_Nan(self):
            self.df = self.df.fillna(0, inplace=True)
            print("fillna fungerar")
        #Ersätter NA-värden med 0

        def clean_data(self):
            self.df = self
            trim_strings = lambda x: x.strip() if isinstance(x, str) else x
            return self.df.applymap(trim_strings)
        #Tar bort mellanslag

        def split_columns(self):
            self.df[{self.column_name}] = self.pd[{self.column_name}].str.split(',', extend = True)
        #Datan ska lagras i en två dimisionell tabell

        def sep_rows(self):
            self.df = self.df.explode("vaccine").reset_index(drop=True)
        #Delar upp listan till rader

        def drop_duplicates(self):
            self.df.drop_duplicates()
        #Droppa dubbletter

class Koronatabeller(Städadata, SqlDatabas):
        def __init__(self, table_name, col, values):
        self.table_name = table_name
        self.col = col
        self.values = values

        def create_tables(self):
            db_con = sqlite3.connect('vaccin_covid.db') 
            cursor = db_con.cursor()
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER PRIMARY KEY, {self.col}, TEXT)")
            db_con.commit()
        #Skapa en tabell

        def insert_to_tables(self):
            db_con = sqlite3.connect('vaccin_covid.db') 
            cursor = db_con.cursor() 
            cursor.execute(f"INSERT INTO {self.table_name} VALUES{self.values}, {self.df}")
            db_con.commit()
        #Sätt in värdena i tabellen


def main():
    start = Koronatabeller("vaccines", "vaccine", "?")
    start.insert_to_tables()
    start_clean_data = Städadata("vaccines")
    start_clean_data.replace_Nan()

if __name__ == "__main__":
    main()