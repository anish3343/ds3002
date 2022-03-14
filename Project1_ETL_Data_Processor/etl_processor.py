"""
Anish Mandalika, am8wk@virginia.edu
DS 3002: Data Science Systems
Data Project 1: ETL Data Processor
"""

import pandas as pd


def processor():
    """ Orchestrates the entire ETL process """

    # Get data from source
    data, input_summary = extract()

    # Transform the data
    transformed_data = transform(data)

    # Generate and print a summary
    summary = "SUMMARY:\n" + input_summary
    print(summary)

def extract():
    """ Gets data from user-entered source and returns it as a DataFrame """

    # Get filetype
    input_type = input("Enter the source file format (One of 'CSV' or 'JSON', case insensitive): ").upper()

    # Get data source
    source = input("Enter a data source, this could be a local file or a URL: ")

    # Get data from the source
    data = pd.DataFrame() # an empty DataFrame to set variable scope

    try:
        if input_type == 'CSV':
            data = pd.read_csv(source)
        elif input_type == 'JSON':
            data = pd.read_json(source)
        else:
            print("ERROR: '" + input_type + "' is not a recognized file format. Please try again with either 'CSV' or 'JSON'.")
            quit()
    except:
        print('ERROR: Something went wrong while trying to read "' + source + '" as a', input_type, "file. Check the dataset and/or filetype and try again.")
        quit()

    # Generate a summary string
    input_summary = 'Input: ' + input_type + ' file with ' + str(len(data)) + ' records and ' + str(len(data.columns)) + ' columns'

    # Print a message indicating end of extraction
    print("Finished extracting data.\n")

    # return the DataFrame and summary string
    return data, input_summary

def transform(data):
    """ Transforms data by adding or removing columns as per user choice """

    # Get desired action from user
    action = input("Please indicate whether you want to add or remove a column (One of 'Add', '+', 'Remove', or '-', case insensitive): ").upper()

    try:
        if action in ['ADD','+']:
            display_cols(data)
            index = int(input('At which index do you want to add a new column? (A number between 0 and ' + str(len(data.columns)) + ', both inclusive)'))
            print('adding')
        elif action in ['REMOVE','-']:
            display_cols(data)
            print('removing')
        else:
            print("ERROR: '" + action + "' is not a recognized action. Please try again with either 'Add', '+', 'Remove', or '-'.")
    except:
        print('ERROR: Something went wrong while trying to add/remove a column. Check the dataset and/or filetype and try again.')
        quit()

    # Print a message indicating end of transformation
    print("Finished transforming data.\n")

    return
    
"""
BEGIN HELPER METHODS
"""

def display_cols(data):
    """ Displays columns in the DataFrame """

    # Print description and header
    print("\nColumns in data:\nPos.\tColumn Name")

    # Print index and column name
    i = 0 # index variable
    for col in data.columns:
        print(i, "\t" + col)
        i += 1

    print('\n')

if __name__ == "__main__":
    try:
        processor()
    except KeyboardInterrupt:
        print("\nProcess aborted by Keyboard Interrupt (Ctrl-C).")
