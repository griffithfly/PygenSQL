# PygenSQL
PygenSQL is based on Python, which aims to provide a way to easy and efficient to automatically create useable SQL queries for users. 
- **Module 1** generates SQL queries for creating tables, which exports a .txt file containing create a new table in a database. 
- **Module 2** runs data assessment for data quality. This module can check fields/variables based on the data dictionary. If any errors are found, a .txt summary report will be generated. Please find error codes overview:
1.	Code 1000 – Check whether the length of columns in a data dictionary and data export is the same. 
2.	Code 1001 – If the length is not the same, the missing column/variable will be shown in the report. 
3.	Code 2000 - check sequence of variables in a data dictionary and data export is the same. If not, the right position(s) will be shown in the report.
4.	Code 3000 - check the range for each column field. For example, if a value is out of range, the ID, wrong value, and suggestion range will be provided in the report.
5.	Code 5000 - check logic for each field. For instance, if column A = 1, column B could not be null. If column B is showing any value, the report will be showing: the ID, value of column A, value of column B, and logical detail.
- **Module 3** provides SQL queries for inserting/updating tables. 

## Module 1 Example

**Module 1** creates a .txt file containing SQL queries. If any field is successfully generated, `field_name [Done]` and total numbers will be shown. 
```
if __name__ == "__main__":
    file = Create_Table()
    loc = file.get_fields('Your_data_dictionary.csv')
    fields = file.genquery_table_dic('Your_data_dictionary.csv')
    print(fields)
```

<img width="993" alt="Screen Shot 2023-04-23 at 1 22 55 AM" src="https://user-images.githubusercontent.com/131559221/233821327-3dfb6e4a-3b2b-4112-afdb-eeb8798433c2.png">

### Module 1 Result (.txt file)
<img width="631" alt="Screen Shot 2023-04-23 at 1 25 25 AM" src="https://user-images.githubusercontent.com/131559221/233821566-98b3d2ae-c883-423e-b15d-c4dce2d023c9.png">


## Module 2 Example

**Module 2** checks values before input data to the database. If any error code(s) showing, the detail can be found in the error report.
```
if __name__ == "__main__":
    files = Check_Table('Your_data_dictionary.csv', 'Your_data_export.csv').check_fields()
    report = Check_Table('Your_data_dictionary.csv', 'Your_data_export.csv').field_report()
    report = Check_Table('Your_data_dictionary.csv', 'Your_data_export.csv').logical_report()
```

<img width="990" alt="Screen Shot 2023-04-23 at 1 40 49 AM" src="https://user-images.githubusercontent.com/131559221/233822046-1c292116-1ebd-482b-ba23-4905ab63b256.png">


### Module 2 Result (.txt file)


<img width="629" alt="Screen Shot 2023-04-23 at 1 49 45 AM" src="https://user-images.githubusercontent.com/131559221/233822394-8a03f7ec-bb58-4754-ad62-c88c16e61e88.png">

## Module 3 Example

**Module 3** provides SQL INSERT INTO statement. 
```
if __name__ == "__main__":
    files = Insert_Table('Your_data_export.csv').sql_insert()
```





