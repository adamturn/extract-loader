# Generic Extract-Loader
Simply extracts all tabular data from any xlsx/pdf file and immediately converts it into a generic csv that is loaded into a Postgres table.

This application utilizes `multiprocessing` from the Python standard library to extract from and load files in parallel.

## Quickstart
Git the code.
```shell
$ cd ~/github/adamturn
$ git clone git@github.com:adamturn/extract-loader.git && cd extract-loader
```

Edit the `pipeline` function in `src/main.py` and pass a database config path to the `from_json` method. Ensure that the table defined in `src/create_table.sql` is created in the same database.
```python
conn = load.DBConfig.from_json("/home/adam/cfg/postgres-test.json").create_psycopg2_connection()
```

Install dependencies and run the code by passing `src/main.py` a directory path.
```shell
(env) $ pip install --upgrade -r requirements.txt
(env) $ python src/main.py /home/adam/io/nyse
```
