# CRUD Operations in SQLite DB using Python and CLI

[![CI](https://github.com/nogibjj/IDS-706_rg361_week-5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS-706_rg361_week-5/actions/workflows/cicd.yml)

This repositroy contains files to perform CRUD (Create-Write-Update-Delete) operations in a ``SQLite`` Database using ``Python`` and ``CLI``

All the CRUD operations are automatically ``logged`` in the ``query_logs`` file.

The base repo has been forked from [sqlite-lab](https://github.com/nogibjj/sqlite-lab) and modified as per requirements.

Forked on on 29-Sep-2023

## Overview

The repository has the ``main.py`` file which makes use of the files in the mylib folder to perform CRUD operations on a SQLite Database. The main.py file can be interacted via ``CLI`` (Command Line Interface) by the user.

The repository automatically **``logs``** all the queries which are executed in the ``query_logs`` file.

``Github`` actions automatically runs the ``test_main.py`` which triggers the CRUD operations and logs them whenever there is an update in the repository.

![Schema](resources/schema.png)

## Instructions

Create a Codespace on main which will initialize the enviroment with the required packages and settings to execute the codes.

The ``main.py`` file accepts the commands via ``CLI``, the CLI are of the form:

```console
python main.py command args
```
the possible commands and their relevant arguments are:
1. ``create``: To crete a Table in a SQLite DB by reading the information from the specified CSV file.<br>Args: (db_name, dataset, auto)
2. ``read``: To run a SQLite READ query entered by the user and return the output.<br>Args: (db_name, table_name, query)
3. ``update``: To run a SQLite UPDATE query entered by the user.<br>Args: (db_name, table_name, query)
4. ``delete``: To run a SQLite DELETE query entered by the user.<br>Args: (db_name, table_name, query)
5. ``create_data``: To create CSV file in the ``Data`` folder from the given source.<br>Args: (source, file_name, auto)
6. ``delete_data``: To delete the CSV file.<br>Args: (file_name, auto)
7. ``clear_log``: To clear the query_logs file.<br>Args: (log_file)

**Notes:** 
- All the arguments to the commands are optional as default values are set in the functions.
- The "auto" argument specfies to the function if the user is directly providing the full path (F) or wants the funtion to use the default path (T). Default value for auto is T

## Sample Execution and Test
  **Sample Execution:** a read command is used without any arguments, so the first 5 rows of the default Database and Table are returned as expected:

   ![Sample_Execution](resources/sample_execution.png)

**Testing:** "make test" command is run to verify all functionalities are working as expected and to see if the CRUD actions are being performed.

**Note:** Coverage is intentioanlly not kept at 100% as we do not call the clear_log funtion which would clear the logs.

![Test Execution](resources/test.png)


## Contents

### 1. query_logs
  Whenever a  CRUD operation is performed, the query is automatically logged in the query_logs file with the timestamp for future reference and use. The log file can be cleared using the ``clear_log`` command

### 2. README.md
   contains the information about the repository and instructions for using it
   
### 3. requirements.txt
   contains the list of packages and libraries which are required for running the project. These are intalled and used in the virtual environment and Github actions.
   
### 4. .github/workflows
   github actions are used to automate the following processes whenever a change is made to the files in the repository:
   - ``install`` : installs the packages and libraries mentioned in the requirements.txt
   - ``test`` : uses ``pytest`` to test the python script and jupyter notebook
      
      **Note:** this action automatically triggers performing CRUD operations whenever any changes are made in the repository
     
   - ``format`` : uses ``black`` to format the python files
   - ``lint`` : uses ``ruff`` to lint the python files
   
     
   **Note** -if all the processes run successfully the following output will be visible in github actions:
   ![Success Build](resources/build.png)
   
### 5. Makefile
   contains the instructions and sequences for the processes used in github actions and .devcontainer for creating the virtual environment
   
### 6. .devcontainer
   contains the ``dockerfile`` and ``devcontainer.json`` files which are used to build and define the setting of the virtual environment (codespaces - python) for running the codes.

### 7. Data
   The CSV files genereated by ``create_data`` are stored here by default for quick access and reference and can be delted using the ``deelte_data`` command

### 8. resources 
   contains additonal files which are used in the README




  
