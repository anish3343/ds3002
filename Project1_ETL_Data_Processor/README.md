# Project 1: ETL Processor

## How to use the ETL Processor

### Installing required packages

This project comes with a `pip` requirements file to ensure all required packages are installed. To use it, run the following on the commandline after ensuring that `python3` and `pip3` are installed:

```bash
pip3 install -r requirements.txt
```

Using a virtual environment is recommended, but by no means neccesary.

### Running the ETL Processor

To run the ETL processor, simply type

```bash
python3 etl_processor.py
```

into a commandline window.

This program does not accept any commandline arguments. Instead, it is a quasi-interactive program that asks for inputs during execution. The inputs asked for during execution are (in order):
- Source file format (`CSV` or `JSON`)
- Source file path
- Whether a column should be added or removed
- Index at which to add/remove a column
- If a column is being added, what the new column should be called
- Destination file format (`CSV`, `JSON` or `SQLite`)
- Destination file path
- If the destination is an `SQLite` file, the name of the destination table

#### Some notes about using the ETL processor

1. There are two sample datasets included with this project: one `CSV` and one `JSON`. However, any `CSV` or `JSON` dataset can be used, and web URLs can be input directly for online datasets. Note that there may be some weird behavior when a file uses encodings other than `utf-8`.
2. When writing to `SQLite`, all columns will be converted to strings to avoid some weirdness with SQAlchemy datatypes.
3. If writing to an existing `SQLite` database, an error will be thrown if a table with the specified name already exists.

## How the ETL Processor works

This ETL processor uses the `pandas` library to ingest, transform and output files.

### Part 1: Extract

Data is read into a `pandas` DataFrame from `CSV` or `JSON` using the `read_csv()` and `read_json()` functions respectively.

### Part 2: Transform

A column is either added to or removed from the DataFrame. If adding, a column containing `NULL` values is inserted at the specified index and the DataFrame expands by one column. If removing, the column at the specified index is removed completely and the DataFrame shrinks by one column.

### Part 3: Load

Transformed data is written to a `CSV`, `JSON` or `SQLite` file using the `to_csv()`, `to_json()` and `to_sql()` functions respectively.