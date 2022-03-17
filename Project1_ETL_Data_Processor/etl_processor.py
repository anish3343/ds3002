"""
Anish Mandalika, am8wk@virginia.edu
DS 3002: Data Science Systems
Data Project 1: ETL Data Processor
"""

import numpy as np
import pandas as pd
from sqlalchemy import create_engine


def processor():
    """ Orchestrates the entire ETL process """

    # Get data from source
    data, input_summary = extract()

    # Transform the data
    transformed_data, transform_summary = transform(data)

    # Load the data into the destination
    load_summary = load(transformed_data)

    # Generate and print a summary
    summary = "\nSUMMARY:\n" + input_summary + transform_summary + load_summary
    print(summary)

def extract():
    """ Gets CSV or JSON data from user-entered source and returns it as a DataFrame """

    # Get filetype
    input_type = input("Enter the source file format (One of 'CSV' or 'JSON', case insensitive): ").upper()

    # Get data source
    source = input("Enter a " + input_type + " data source, this could be a local file or a URL: ")

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
    except FileNotFoundError:
        print("ERROR: No file was found at", source + '. Please double check the data source and try again.')
        quit()
    except Exception as e:
        print('ERROR: Something went wrong while trying to read "' + source + '" as a', input_type, "file. Check the dataset and/or filetype and try again.\nType of error:", e)
        quit()

    # Generate a summary string
    summary = 'Input: ' + input_type + ' file with ' + str(len(data)) + ' records and ' + str(len(data.columns)) + ' columns from "' + source + '" read as a DataFrame.\n'

    # Print a message indicating end of extraction
    print("Finished extracting data.\n")

    # return the DataFrame and summary string
    return data, summary

def transform(data):
    """ Transforms data by adding or removing columns as per user choice """

    # Get desired action from user
    action = input("Please indicate whether you want to add or remove a column (One of 'Add', '+', 'Remove', or '-', case insensitive): ").upper()

    # Construct summary string
    summary = "Transformation: "

    # Display current columns, ask user for desired add/remove index and add/remove column.
    try:
        if action in ['ADD','+']:
            display_cols(data)
            index = int(input('At which index do you want to add a new column? (A number between 0 and ' + str(len(data.columns)) + ', both inclusive): '))
            if index < 0 or index > len(data.columns):
                raise ValueError('value out of bounds: index ' + str(index) + ' is not between 0 and ' + str(len(data.columns)))
            col_name = input('What should the new column be called?: ')
            data.insert(index, col_name, np.nan)
            summary = summary + "Added column '" + col_name + "' at index " + str(index)
        elif action in ['REMOVE','-']:
            display_cols(data)
            index = int(input('At which index do you want to remove a column? (A number between 0 and ' + str(len(data.columns)-1) + ', both inclusive): '))
            if index < 0 or index > (len(data.columns)-1):
                raise ValueError('value out of bounds: index ' + str(index) + ' is not between 0 and ' + str(len(data.columns)-1))
            col_name = data.columns[index]
            data.drop(col_name, axis=1, inplace=True)
            summary = summary + "Removed column '" + col_name + "' at index " + str(index)
        else:
            print("ERROR: '" + action + "' is not a recognized action. Please try again with either 'Add', '+', 'Remove', or '-'.")
    except ValueError as e:
        print('ERROR: You did not enter a valid number. Please check your inputs and try again.\nType of error:', e)
        quit()
    except Exception as e:
        print('ERROR: Something went wrong while trying to add/remove a column. Check the dataset and/or filetype and try again.\nType of error:', e)
        quit()

    # Print a message indicating end of transformation
    print("Finished transforming data.\n")

    # Format the summary string and return it along with the data
    summary = summary + '.\n'
    return data, summary
    
def load(data):
    """ loads data into a CSV, JSON or SQL file per user choice. """

    # Get output filetype from user
    output_type = input("Enter the destination file format (One of 'CSV' ,'JSON' or 'SQLite', case insensitive): ").upper()

    # Get destination
    destination = input("Enter a filename for your " + output_type + " file WITHOUT any extensions: ")

    # Write output
    try:
        if output_type == 'CSV':
            destination = destination + '.csv'
            data.to_csv(destination)
        elif output_type == 'JSON':
            destination = destination + '.json'
            data.to_json(destination)
        elif output_type == 'SQLITE':
            destination = destination + '.db'
            engine = create_engine('sqlite:///'+destination)
            sqlite_connection = engine.connect()
            sqlite_table = input('Enter the name of the table where this data should be stored (An error will be thrown if this table already exists in ' + destination + '): ')
            data = data.astype(str)
            data.to_sql(sqlite_table, sqlite_connection, if_exists='fail')
            sqlite_connection.close()
        else:
            print("ERROR: '" + output_type + "' is not a recognized file format. Please try again with 'CSV', 'JSON' or 'SQLite'.")
            quit()
    except Exception as e:
        print('ERROR: Something went wrong while trying to write a ' + output_type + ' file to "' + destination + "\". Check the dataset and/or filetype and try again.\nType of error:", e)
        quit()

    # Print message indicating end of load phase
    print('Finished writing data.')

    # Construct summary string
    summary = "Output: DataFrame with " + str(len(data)) + ' records and ' + str(len(data.columns)) + ' columns written as a ' + output_type + ' file to "' + destination + '".\n'
    
    return summary

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

    print()

if __name__ == "__main__":
    try:
        processor()
    except KeyboardInterrupt:
        print("\nProcess aborted by Keyboard Interrupt (Ctrl-C).")
    except Exception as e:
        print("ERROR: Something went wrong.\nType of error: ", e)
