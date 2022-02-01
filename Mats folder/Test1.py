import pandas as pd
import sqlite3

class databashantering():
    def __init__(self, db_name:str, csv:str, CSV:str, table_name):
        self.db_name = db_name
        self.csv = csv
        self.table_name = table_name
        self.df = pd.read_csv("vaccin_covid.csv") #self.csv
        self.db = sqlite3.connect("vaccin_covid.db") #self.db_name
        self.cur =self.db.cursor()

    def seperate(self, column_name, seperator):
        self.column_name = column_name
        self.seperator = seperator
        splittad = self.df[self.coulmn_name] .str.split(self.seperator, expand=True)
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




def smallest(list):
    min= list[0]
    for i in list:
        if i<small:
            small=i
    return small
    """De här en string som ska jämför värdena i doc stringen, 
    vi ska jämföra för att se vilket som är lägst
    """

def main():
    print("I'm in the main method")
    
    a = 100
    b = 1000
    c = 10000
    list = [a, b, c]
    print("smallest in ",list,"is")
    print(min(list))


if __name__ == "__main__":
    main() # call on the main function



    """Test.py

import pandas as pd
import sqlite3

corona_vacc_df = pd.read_csv('data/vaccin_covid.csv')
db_connect = sqlite3.connect("corona_vacc.db")
cursor = db_connect.cursor()
corona_vacc_df.to_sql('corona_vacc', db_connect)
print(corona_vacc_df.head)
db_connect.commit()
"""
#def compare_smallest_value(first_string: int, second_string: int, third_string: int)
    """De här en string som ska jämför värdena i doc stringen, 
    vi ska jämföra för att se vilket som är lägst"""

