"""
Test Script for Main Code and Lib Files.
The main file calls the libs files hence no separate test file for libs.
"""

import subprocess
import os


def test_main():
    # log file check
    # check if log file already exists

    # delete Data file
    if os.path.exists("./Data/Master.csv"):
        os.remove("./Data/Master.csv")

    # check creation of Data file
    result = subprocess.run(
        [
            "python",
            "main.py",
            "create_data",
            "https://github.com/Opensourcefordatascience/Data-sets/raw/master/automotive_data.csv",
            "./Data/Master.csv",
            "F",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "processed" in result.stdout
    assert os.path.exists("./Data/Master.csv")

    # check creation of DB file
    result = subprocess.run(
        ["python", "main.py", "create", "Master.db", "./Data/Master.csv", "F"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "created" in result.stdout
    assert os.path.exists("./Master.db")

    # check read from DB file
    result = subprocess.run(
        [
            "python",
            "main.py",
            "read",
            "Master.db",
            "Master",
            "SELECT * FROM Master LIMIT 1",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "(1, '3', '?', 'alfa-romero'" in result.stdout

    # check update from DB file
    result = subprocess.run(
        [
            "python",
            "main.py",
            "update",
            "Master.db",
            "Master",
            "UPDATE Master SET make = 'alfa_romero' WHERE make = 'alfa-romero'",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    result = subprocess.run(
        [
            "python",
            "main.py",
            "read",
            "Master.db",
            "Master",
            "SELECT * FROM Master LIMIT 1",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "(1, '3', '?', 'alfa_romero'" in result.stdout

    # check delete from DB file
    result = subprocess.run(
        [
            "python",
            "main.py",
            "delete",
            "Master.db",
            "Master",
            "DELETE FROM Master WHERE make = 'alfa_romero'",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    result = subprocess.run(
        ["python", "main.py", "read", "Master.db", "Master", "SELECT * FROM Master"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "alfa_romero" not in result.stdout

    print("manual Checks complete")
    print("checking auto generation")
    # checking autocase of files
    subprocess.run(["python", "main.py", "delete_data"])
    subprocess.run(["python", "main.py", "create_data"])
    subprocess.run(["python", "main.py", "create"])
    subprocess.run(["python", "main.py", "read"])
    subprocess.run(["python", "main.py", "update"])
    subprocess.run(["python", "main.py", "delete"])

    # assert output after expected auto generation
    result = subprocess.run(
        [
            "python",
            "main.py",
            "read",
            "Master.db",
            "Master",
            "SELECT * FROM Master LIMIT 1",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "(2, '3', 'Unknown', 'alfa-romero'" in result.stdout
    assert "(1, '3', 'Unknown', 'alfa-romero'" not in result.stdout

    # testing error messages
    result = subprocess.run(
        ["python", "main.py", "read", "Master.db", "Master", "testing error"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Invalid Query" in result.stdout

    result = subprocess.run(
        ["python", "main.py", "read", "Master.db", "Master", "READ testing error"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Invalid Query" in result.stdout


if __name__ == "__main__":
    test_main()
    pass
