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

