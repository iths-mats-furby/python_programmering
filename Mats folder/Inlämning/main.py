import pandas as pd
import sqlite3
from Test1 import databashantering
#from test 
#from pathlib import Path

def main():
    db = databashantering()
    #db = pd.read_csv('vaccin_covid.csv') #seed_database()
    #self.df = pd.read_csv('vaccin_covid.csv')
    db.table_create_and_insert() #create_database ()
    #db = ("vaccin_covid.csv")  #databashantering = sqlite3.connect("corona_vacc.db") # ("corona_vacc.db")
    #db = databashantering # ("corona_vacc.db")
    
    print("Hello main!") # Will be printed
    #db.create.database()
    #vax.col()b
#corona_vacc_df.head()
    db.table_create_and_insert() #create_database ()
if __name__ == "__main__":
    main() # Call on the main function



import pandas as pd
import sqlite3
from Test1 import databashantering
#from test 
#from pathlib import Path

def main():
    db = databashantering()
    self.df = db.Test1('vaccin_covid.csv') 
    #self.df = pd.read_csv('vaccin_covid.csv')
    #Read filen räcker väl att ha i klassen?
    #self.df = db.Test1("/Users/hjalp/OneDrive/Dokument/Personligt/Data/EC/Python/Data/git/python_programmering/Mats folder/vaccin_covid.csv")
    #1 I uppgiften framgår att man ska "läsa in csv filen" i mainfilen 
    db.table_create_and_insert() #create_database (tab_name, groupselect_table1, AVGselect_table2))
    #2 Skapa och använda datahanterings-klassen för att utföra sitt arbete
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

