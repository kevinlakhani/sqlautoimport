# <img src="https://raw.githubusercontent.com/kevinlakhani/sqlautoimport/1fb8a56c1e288cacfbc07ba997b5656be08c16e7/icon/icon.svg" alt="icon" height="30"/> SQL Auto Import (sqlautoimport)
SQL Auto Import is a command-line interface (CLI) tool, written in [Python](https://www.python.org/)®, that allows you to quickly create/populate or replace tables in a SQL database with multiple CSV files.

PostreSQL, MySQL, SQLite, MSSQL (Microsoft SQL Server/T-SQL), and Oracle dialects are supported.

SQL Auto Import is available for Windows, macOS, and Linux

# Downloads
Note: When opening a portable executable file, allow a few moments for initialization.

## Windows

Download: [Portable 64-bit executable file (.exe)](https://github.com/kevinlakhani/sqlautoimport/raw/master/sqlautoimport.exe)
Download: [Portable 32-bit executable file (.exe)](https://github.com/kevinlakhani/sqlautoimport/raw/master/sqlautoimport-32.exe)

## macOS, Linux, and others
In progress. 

For now, use [sqlautoimport.py](https://github.com/kevinlakhani/sqlautoimport/blob/master/sqlautoimport.py) with Python. 

Dependencies listed in [requirements.txt](https://github.com/kevinlakhani/sqlautoimport/blob/master/requirements.txt) will also need to be installed.

# Usage
Open Command Prompt in the directory your copy of `sqlautoimport.exe` (or `sqlautoimport-32.exe`) is located. Alternatively, you can point the Command Prompt to the full directory path where your executable is located.

For regular usage, you must specify the FLAVOR, HOST, PORT, DATABASE, USERNAME, and PASSWORD to connect to. 

Current supported FLAVOR options are:
`postgresql`, `mysql`, `sqlite` ,`oracle`, and `mssql`
Which correspond to
[PostgreSQL](https://www.postgresql.org/), [MySQL](https://www.mysql.com/), [SQLite](https://sqlite.org), [Oracle](https://oracle.com), and [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/default.aspx). More flavor compatibility is coming soon.

You will probably also want to include the DIRECTORY where your files are located, but if you don't it will be assumed that the local directory contains the files you want to import to your database. 

Here's an example command:
```
sqlautoimport.exe --directory "C:\My Files" --flavor mysql --host my.host.com --port 3306 --database db --username u --password p
```

Additionally, be sure to use the `--schema` argument if you need to load files into a schema in your database other than its default schema.

While SQL Auto Import expects a comma-delimited, CSV (`.csv`) file by default, you can specify a different file extension through the `--extension` argument. If your files are not comma-delimited, you will also need to use the `--delimiter`argument. For example, for tab-separated files use `--delimiter \t`. For pipe-delimited files, use `--delimiter |`.

There are additional options to help with flexibility and automation needs, such as `-s` and `-y`. For more information, use the `--help` argument. Its full output is shown below for your convenience:
```
usage: sqlautoimport [--license] [-h] [-v] --flavor
                     {postgres,postgresql,mysql,sqlite,sqlite3,oracle,mssql}
                     --host HOST --port PORT --database DATABASE --username
                     USERNAME --password PASSWORD [--directory DIRECTORY]
                     [--schema SCHEMA] [--delimiter DELIMITER]
                     [--extension EXTENSION] [-q] [-s] [-y]

SQL Auto Import v 2.0.0

Special Arguments:
  --license             View license and copyright info. All other arguments
                        ignored.
  -h, --help            Show this help message and exit.
  -v, -V, --version     Show the version number.

Required Arguments:
  --flavor {postgres,postgresql,mysql,sqlite,sqlite3,oracle,mssql}
                        SQL flavor.
  --host HOST           Server hosts internet address (IP or URL).
  --port PORT           Hosts port.
  --database DATABASE   Destination database name.
  --username USERNAME   Username with access to database.
  --password PASSWORD   Password corresponding to username.

Recommended Arguments:
  --directory DIRECTORY
                        Source file(s) directory. Defaults to local directory.
  --schema SCHEMA       Database schema. If not specified, default schema will
                        be used.

Optional Arguments:
  --delimiter DELIMITER
                        Source file(s) delimiter. Comma (,) by default.
  --extension EXTENSION
                        Source file(s) extension. Defaults to csv.
  -q, --quiet           Quiet mode. Minimal ouput.
  -s, --silent          Silent mode. No output except confirmations.
  -y, --yes             Skip all confirmations. WARNING: This is dangerous.
```


# Roadmap
 - [x] ~~Implement `argparse` library for more flexible command-line usage~~ 
	 - [x] ~~Support for different delimiters and file extensions (e.g. `.tsv`)~~
	 - [x] ~~Support for specifying modes other than `replace` (e.g. `append`)~~
	 - [ ] Support for `.json` files
	 - [x] ~~Support for schema specification~~
	 - [ ] Performance tuning: specify chunk size and/or auto-select settings based on data size
 - [ ] macOS and Linux packages/bundled executables
 - [ ] Automated unit and functional tests
 - [ ] Support for Redshift, Presto and [other "external" dialects](https://docs.sqlalchemy.org/en/13/dialects/#external-dialects)
 - [ ] Override default column type settings (e.g. specify a column as `money` instead of `double` or `smallint` instead of `bigint`)
 - [ ] Web GUI

# Attributions
SQL Auto Import ("sqlautoimport") uses the following open-source libraries, each of which have their own copyright and license:

 - **pandas**
	 - License: [https://github.com/pandas-dev/pandas/blob/master/LICENSE](https://github.com/pandas-dev/pandas/blob/master/LICENSE)
	 - Copyright
		 - Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team. All rights reserved.
		 - Copyright (c) 2011-2020, Open source contributors.
 - **NumPy**
 	 - License: https://github.com/numpy/numpy/blob/master/LICENSE.txt
	 - Copyright: Copyright (c) 2005-2020, NumPy Developers.
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
- **Python** and any Python built-in libraries:
	- License: [https://docs.python.org/3.7/license.html](https://docs.python.org/3.7/license.html)
	- Additional info: [https://wiki.python.org/moin/PythonSoftwareFoundationLicenseFaq](https://wiki.python.org/moin/PythonSoftwareFoundationLicenseFaq) 

[PyInstaller](https://github.com/pyinstaller/pyinstaller) is used for building packaged executables.

"Python" is a registered trademark of the [Python Software Foundation]([https://www.python.org/psf/)


```
 _____  _____  _
/  ___||  _  || |
\ `--. | | | || |
 `--. \| | | || |
/\__/ /\ \/' /| |____
\____/  \_/\_\\_____/
  ___          _
 / _ \        | |
/ /_\ \ _   _ | |_   ___
|  _  || | | || __| / _ \
| | | || |_| || |_ | (_) |
\_| |_/ \__,_| \__| \___/
 _____                                 _
|_   _|                               | |
  | |   _ __ ___   _ __    ___   _ __ | |_
  | |  | '_ ` _ \ | '_ \  / _ \ | '__|| __|
 _| |_ | | | | | || |_) || (_) || |   | |_
 \___/ |_| |_| |_|| .__/  \___/ |_|    \__|
                  | |
                  |_|
```