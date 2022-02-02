import pandas as pd
import sqlite3

class databashantering():
    def __init__(self, db_name:str, csv:str, CSV:str, table_name):
        self.db_name = db_name
        self.csv = csv
        self.table_name = table_name
        self.df = pd.read_csv(self.csv) #self.csv
        self.db = sqlite3.connect(self.db_name)  #"vaccin_covid.db"
        self.cur = self.db.cursor()

    def seperate(self, column_name, seperator):
        self.column_name = column_name
        self.seperator = seperator
        splittad = self.df[self.column_name] .str.split(self.seperator, expand=True)
        self.df = self.df.join(splittad)
        del self.df[self.column_name]

    def seed_database(self):
        self.df.to_sql(self.table_name, self.db)
        self.db.commit()
    
    def table_create_and_insert(self, tab_name, groupselect_table1, AVGselect_table2):
        self.groupselect_table1 = groupselect_table1
        self.AVGselect_table2 =AVGselect_table2
        self.tab_name = tab_name
        self.cur.execute("""CREATE TABLE {self.tab.name}, AS SELECT DISTINCT {self.groupselect_table1}, 
        AVG({self.groupselect_table1}), GROUP BY {groupselect_table1}""")