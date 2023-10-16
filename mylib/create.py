"""
Creates a new Sqlite3 Database by reading the CSV Data
"""
import sqlite3
import csv
from logs import write_log


def create_db(db_name="Master.db", dataset="Master.csv", auto="T"):
    if auto in ["T", "t"]:
        dataset = "./Data/{}".format(dataset)

    # read csv
    payload = csv.reader(open(dataset, newline=""), delimiter=",")

    # create dynaic headers to use in query
    for row in payload:
        header = row
        break
    col_names = ""
    for i in header:
        col_names += i + ", "
    col_names = col_names[:-2]
    col_names = col_names.replace("-", "_")
    col_holder = "(" + ("?," * len(header))[:-1] + ")"

    # write to DB
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Master")

    create_query = (
        "CREATE TABLE Master (id INTEGER PRIMARY KEY AUTOINCREMENT," + col_names + ")"
    )

    c.execute(create_query)
    write_log(create_query)

    # insert
    insert_query = "INSERT INTO Master(" + col_names + ")" + " VALUES " + col_holder
    c.executemany(insert_query, payload)
    conn.commit()
    conn.close()
    write_log(insert_query)
    pass


if __name__ == "__main__":
    create_db()
    pass
