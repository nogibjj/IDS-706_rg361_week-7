"""
Query Scripts Using SQLite and Python which can be exceuted via CLI
"""

# Import libraries
import sys
import argparse

sys.path.insert(0, "./mylib")

# Import Custom Libraries functions
from mylib.logs import clear_log  # noqa: E402
from mylib.data_csv import create_data, delete_data  # noqa: E402
from mylib.create import create_db  # noqa: E402
from mylib.read import read_db  # noqa: E402
from mylib.update import update_db  # noqa: E402
from mylib.delete import delete_record  # noqa: E402


def handle_arguments(args):
    """To Handle initial arguments"""
    parser = argparse.ArgumentParser(description="CRUD Operations on SQLite DB")
    parser.add_argument(
        "action",
        choices=[
            "create",
            "read",
            "update",
            "delete",
            "create_data",
            "delete_data",
            "clear_log",
        ],
    )
    args = parser.parse_args(args[:1])
    print(args.action)
    if args.action == "create":
        parser.add_argument("db_name", type=str, nargs="?", default="Master.db")
        parser.add_argument("dataset_name", type=str, nargs="?", default="Master.csv")
        parser.add_argument("auto", type=str, nargs="?", default="T")

    elif args.action in ["read", "update", "delete"]:
        parser.add_argument("db_name", type=str, nargs="?", default="Master.db")
        parser.add_argument("table_name", type=str, nargs="?", default="Master")
        parser.add_argument("query", type=str, nargs="?", default=None)
    elif args.action == "create_data":
        parser.add_argument(
            "source",
            type=str,
            nargs="?",
            default="https://github.com/Opensourcefordatascience/Data-sets/raw/master/automotive_data.csv",
        )
        parser.add_argument("file_name", type=str, nargs="?", default="Master.csv")
        parser.add_argument("auto", type=str, nargs="?", default="T")
    elif args.action == "delete_data":
        parser.add_argument("file_name", type=str, nargs="?", default="Master.csv")
        parser.add_argument("auto", type=str, nargs="?", default="T")
    elif args.action == "clear_log":
        parser.add_argument("log_file", type=str, nargs="?", default="./query_logs.md")

    # parse again with ever
    return parser.parse_args(sys.argv[1:])


def main():
    """To call other fucntions based on the arguments"""

    args = handle_arguments(sys.argv[1:])

    if args.action == "create":
        print("creating...")
        create_db(args.db_name, args.dataset_name, args.auto)
        return "created"
    elif args.action == "read":
        print("processing...")
        return read_db(args.db_name, args.table_name, args.query)

    elif args.action == "update":
        print("processing...")
        return update_db(args.db_name, args.table_name, args.query)

    elif args.action == "delete":
        print("processing...")
        return delete_record(args.db_name, args.table_name, args.query)

    elif args.action == "create_data":
        print("processing...")
        create_data(args.source, args.file_name, args.auto)
        return "processed"
    elif args.action == "delete_data":
        print("processing...")
        delete_data(args.file_name, args.auto)
        return "processed"
    elif args.action == "clear_log":
        print("processing...")
        clear_log(args.log_file)
        return "processed"
    else:
        return f"Unknown Input: {args.action}"


if __name__ == "__main__":
    print(main())
