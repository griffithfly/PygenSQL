# PygenSQL
PygenSQL is based on Python, which aims to provide a way to easy and efficient to automatically create useable SQL queries for users

## Module 1 Example

The first module is created a .txt file containing SQL queries. If any field is successfully generated, the total numbers and field_name and [Done] will be showing. Please find the screenshot 1.
```
if __name__ == "__main__":
    file = Create_Table()
    loc = file.get_fields('Your_data_dictionary.csv')
    fields = file.genquery_table_dic('Your_data_dictionary.csv')
    print(fields)
```
