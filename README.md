# PygenSQL
PygenSQL is based on Python, which aims to provide a way to easy and efficient to automatically create useable SQL queries for users. 
- **Module 1** generates SQL queries for creating tables, which exports a .txt file containing create a new table in a database. 
- **Module 2** runs data assessment for data quality. This module can check fields/variables based on the data dictionary. If any errors are found, a .txt summary report will be generated. 
- **Module 3** provides SQL queries for inserting/updating tables. 

## Module 1 Example

The first module creates a .txt file containing SQL queries. If any field is successfully generated, `field_name [Done]` and total numbers will be shown. 
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

