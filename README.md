# PygenSQL
PygenSQL is based on Python, which aims to provide a way to easy and efficient to automatically create useable SQL queries for users

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

## Module 2 Example

