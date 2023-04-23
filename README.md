# PygenSQL
PygenSQL is based on Python, which aims to provide a way to easy and efficient to automatically create useable SQL queries for users

## Module 1 Example

```
if __name__ == "__main__":
    file = Create_Table()
    loc = file.get_fields('Your_data_dictionary.csv')
    fields = file.genquery_table_dic('Your_data_dictionary.csv')
    print(fields)
```
