# PygenSQL
PygenSQL is based on Python, which aims to provide a way to easy and efficient to automatically create useable SQL queries for users

## Module 1 Example

The first module is created a .txt file containing SQL queries. If any field is successfully generated, `field_name [Done]` and total numbers will be showing. 
```
if __name__ == "__main__":
    file = Create_Table()
    loc = file.get_fields('Your_data_dictionary.csv')
    fields = file.genquery_table_dic('Your_data_dictionary.csv')
    print(fields)
```

<img width="437" alt="Picture1" src="https://user-images.githubusercontent.com/131559221/233821141-6f9f8e16-0c57-404e-9036-efb644229c82.png">

