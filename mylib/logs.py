"""
To write the query logs to the log file
"""
from datetime import datetime


def write_log(query, log_file="./query_logs.md"):
    """
    To write the query logs to the log file
    """
    now = datetime.now()
    dt_string = now.strftime("%d-%b-%Y %H:%M") + " (UTC)"

    with open(log_file, "a") as file:
        file.write(f"{dt_string}:\n```sql\n{query}\n```\n\n")
        file.write("\n")
        file.close()
    pass


def clear_log(log_file="./query_logs.md"):
    """
    To clear the query logs from the log file
    """
    open(log_file, "w").close()
    pass


if __name__ == "__main__":
    write_log("testing log file")
    clear_log()
    pass
