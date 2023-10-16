"""
File to read data from a DB
"""

import sqlite3
from logs import write_log


def read_db(db_name="Master.db", table_name="Master", query=None):
    """
    Read from a DB, if no query is provided, it will return the first 5 rows
    """
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    if query is None:
        query = "SELECT * FROM " + table_name + " LIMIT 5;"
    if not query.lower().startswith("select"):
        return "Invalid Query, Read operations should start with SELECT"

    try:
        c.execute(query)
        payload = c.fetchall()
    except Exception:
        payload = "Invalid Query"
    conn.commit()
    conn.close()
    write_log(query)
    return payload


if __name__ == "__main__":
    print(read_db())
    pass
