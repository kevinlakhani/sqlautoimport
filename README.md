
# SQL Auto Import (sqlautoimport)
Welcome to the SQL Auto Import tool. This command-line tool, written in Python®, allows you to quickly create/populate or replace tables in a SQL database with CSV files.

PostreSQL, MySQL, SQLite, MSSQL, and Oracle dialects are supported.

This tool will attempt to load connection settings from a config.json file by default. You can specify
a file to use as a command line argument. If no file is found or if there is an issue, you will be asked
to input the information below. You will have the options to save the connection settings. 

Additionally, you will need to specify a directory path to your CSV files (e.g. C:\MyFiles). You can
also pass this in as a second command-line argument. 

If you do not enter a path, the local directory will be used.

This tool will use the names of your files as table names (in lowercase), so make sure they're correct. If a table already exists, it will be replaced.

Only the default schema is currently supported.

# Usage
The source Python file (.py) is provided, which can be used on any system where Python is installed. For Windows users who do not wish to use or install Python, an executable file (.exe) is provided in the /dist/ folder ([or just download it here](https://github.com/kevinlakhani/sqlautoimport/raw/master/dist/sqlautoimport.exe)).

Using the .exe file requires Microsoft Visual C++ to be installed on your system.

The when using the .py or .exe file, two arguments may be passed:

 1. The file path of the config file containing connection details
 2. The folder path of the CSV files to be imported to your database

If these arguments are not passed or if there is an issue with them, you will be prompted to enter those details.

# Attributions
SQL Auto Import (sqlautoimport) is uses the following open-source libraries, each of which have their own copyright and license:

 - **pandas**
	 - License: [https://github.com/pandas-dev/pandas/blob/master/LICENSE](https://github.com/pandas-dev/pandas/blob/master/LICENSE)
	 - Copyright
		 - Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team. All rights reserved.
		 - Copyright (c) 2011-2020, Open source contributors.
 - **sqlalchemy**
	 - License [https://github.com/sqlalchemy/sqlalchemy/blob/master/LICENSE](https://github.com/sqlalchemy/sqlalchemy/blob/master/LICENSE)
	 - Copyright:
		 - Copyright 2005-2020 SQLAlchemy authors and contributors \<see AUTHORS file>.
- **tqdm**
	- License: [https://github.com/tqdm/tqdm/blob/master/LICENCE](https://github.com/tqdm/tqdm/blob/master/LICENCE)
	- Copyright:
		- MPLv2.0 2015-2020 (c) Casper da Costa-Luis
		- MIT 2016 (c) [PR #96] on behalf of Google Inc.
		- MIT 2013 (c) Noam Yorav-Raphael, original author.
- **psycopg2**
	 - License: 
		 - [https://github.com/psycopg/psycopg2/blob/master/LICENSE](https://github.com/psycopg/psycopg2/blob/master/LICENSE)
		 - [https://www.psycopg.org/license/](https://www.psycopg.org/license/)
	 - Copyright:
		 - ?
 -  **sqlite3**
	 - License: [https://www.sqlite.org/copyright.html](https://www.sqlite.org/copyright.html)
	 - Copyright:
		 - Public Domain
- **pyodbc**
	- License: [https://github.com/mkleehammer/pyodbc/blob/master/LICENSE.txt](https://github.com/mkleehammer/pyodbc/blob/master/LICENSE.txt)
- **cx_Oracle**
	- License: [https://github.com/oracle/python-cx_Oracle/blob/master/LICENSE.txt](https://github.com/oracle/python-cx_Oracle/blob/master/LICENSE.txt)
	- Copyright: 
		- Copyright 2016, 2018, Oracle and/or its affiliates. All rights reserved.
		- Portions Copyright 2007-2015, Anthony Tuininga. All rights reserved.
		- Portions Copyright 2001-2007, Computronix (Canada) Ltd., Edmonton, Alberta, Canada. All rights reserved.
- **mysqlclient**:
	- License: [https://github.com/PyMySQL/mysqlclient-python/blob/master/LICENSE](https://github.com/PyMySQL/mysqlclient-python/blob/master/LICENSE)
- **os**, **time**, **json**, **sys**, and any other Python built-in libraries:
	- License: [https://wiki.python.org/moin/PythonSoftwareFoundationLicenseFaq](https://wiki.python.org/moin/PythonSoftwareFoundationLicenseFaq) 

"Python" is a registered trademark of the Python Software Foundation

# Roadmap
 - Support for schema specification
 - Support for .json files
 - Support for specifying modes other than "replace" (e.g. "append")
