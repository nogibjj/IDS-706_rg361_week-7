"""
To Delete Records or Tables from the Database
"""
import sqlite3
from logs import write_log


def delete_record(db_name="Master.db", table_name="Master", query=None):
    """
    To Delete Records or Tables from the Database
    """
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    if query is None:
        query = """DELETE FROM """ + table_name + """ WHERE "id" IS 1;"""

    if not query.lower().startswith("delete"):
        return "Invalid Query, Expected to start with DELETE"
    try:
        c.execute(query)
        payload = "Success"
    except Exception:
        payload = "Invalid Query"
    conn.commit()
    conn.close()
    write_log(query)
    return payload


if __name__ == "__main__":
    print(delete_record())
    pass
