"""
To perform the update operations on the database
"""
import sqlite3
from logs import write_log


def update_db(db_name="Master.db", table_name="Master", query=None):
    """
    To perform the update operations on the database
    """
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    if query is None:
        query = (
            """UPDATE """
            + table_name
            + """ SET "normalized_losses" = 'Unknown'  
            WHERE "normalized_losses" IS "?";"""
        )
    if not query.lower().startswith(("update", "insert")):
        return "Invalid Query, Expected to start with UPDATE or INSERT"
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
    print(update_db())
    pass
