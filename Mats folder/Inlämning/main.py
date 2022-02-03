from klass import Koronatabeller

def main():
    start = Koronatabeller("vaccines", "vaccine", "?")
    start.insert_to_tables()
    start_clean_data = CleanData("vaccines")
    start_clean_data.replace_Nan()

if __name__ == "__main__":
    main()