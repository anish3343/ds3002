"""
Anish Mandalika, am8wk@virginia.edu
DS 3002: Data Science Systems
Data Project 1: ETL Data Processor
"""

import pandas as pd

def processor():

    # Get data from source
    data = get_data()

"""
Get data from user-entered source and return it as a DataFrame
"""
def get_data():

    # Get filetype
    input_type = input("Enter the source file format (One of CSV, JSON or SQL): ").upper()

    # Get data source
    source = input("Enter a data source, this could be a local file or a URL: ")

    # Get data from the source
    if(input_type == "CSV"):
        try:
            data = pd.read_csv(source)
            print(data)
        except:
            print("ERROR: Something went wrong while trying to read", source, "as a CSV file. Check the dataset and/or filetype and try again.")

    
    

if __name__ == "__main__":
    try:
        processor()
    except KeyboardInterrupt:
        print("\nProcess aborted by Keyboard Interrupt (Ctrl-C).")
