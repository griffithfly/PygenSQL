# Test Module 1

import Creat_SQL_table as ct

file = ct.Create_Table()
loc = file.get_fields('your_data_dictionary.xlsx')
fields = file.genquery_table_dic('your_data_dictionary.xlsx')
print(fields)


# Test Module 2

import Data_Validation as dv

files = dv.Check_Table('your_data_dictionary.csv', 'your_data_export.csv').check_fields()
report = dv.Check_Table('your_data_dictionary.csv', 'your_data_export.csv').field_report()
report = dv.Check_Table('your_data_dictionary.csv', 'your_data_export.csv').logical_report()

# Test Module 3

import Update_SQL_Statement as up

files = up.Insert_Table('your_data_export.csv').sql_insert()
