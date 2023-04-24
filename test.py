# Test Module 1

import Creat_SQL_table as ct
'''
'your_data_dictionary.xlsx' is a data dictionary file. 
A standard example(example_data_dictionary.xlsx) was provide in this repository.
'''
file = ct.Create_Table()
loc = file.get_fields('your_data_dictionary.xlsx')
fields = file.genquery_table_dic('your_data_dictionary.xlsx')
print(fields)

## For example, copy & paste following code to your local. Please make sure 'example_data_dictionary.xlsx' in the same directory.

import pandas as pd
import Creat_SQL_table as ct

unit_test = pd.read_excel('example_data_dictionary.xlsx')
file = ct.Create_Table()
loc = file.get_fields('example_data_dictionary.xlsx')
fields = file.genquery_table_dic('example_data_dictionary.xlsx')
print(fields, len(unit_test)) # Output: (['visitid [Done]', 'SYS_LOC_CODE [Done]', 'marital_status [Done]', 'conc [Done]', 'analyte [Done]'], 5) 5

## A .txt file will be created in the same directory containing SQL queries for creating a table.
## The First 5 is 5 fields were successfully processed. The second 5 is the length of fields in the data dictionary file.
## Numbers are the same means all variables are processed.


# Test Module 2

import Data_Validation as dv

files = dv.Check_Table('your_data_dictionary.csv', 'your_data_export.csv').check_fields()
report = dv.Check_Table('your_data_dictionary.csv', 'your_data_export.csv').field_report()
report = dv.Check_Table('your_data_dictionary.csv', 'your_data_export.csv').logical_report()

## A error log (.txt file) will be created in the same directory containing details of errors(Code 1000, Code 1001, Code 2000, Code 3000, and Code 5000)
## Please find details of code 1000 - code 5000 in the README.md

# Test Module 3

import Update_SQL_Statement as up

files = up.Insert_Table('your_data_export.csv').sql_insert()
## A .txt file will be created in the same directory containing SQL queries for inerterting data to the table.
