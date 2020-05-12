
# <img src="https://raw.githubusercontent.com/kevinlakhani/sqlautoimport/1fb8a56c1e288cacfbc07ba997b5656be08c16e7/icon/icon.svg" alt="icon" height="30"/> SQL Auto Import (sqlautoimport)
SQL Auto Import is a command-line interface tool, written in [Python](https://www.python.org/)®, that allows you to quickly create, populate, and/or replace tables in a SQL database with multiple source files.

This alleviates the hassle of manually writing `CREATE TABLE` statements and laboriously importing files one-by-one. Just point the SQL Auto Import tool to the directory containing your files and enter your database credentials - let SQL Auto Import do the rest.

PostreSQL, MySQL, SQLite, MSSQL (Microsoft SQL Server/T-SQL), and Oracle SQL flavors are supported. More flavors are on the [project roadmap](#roadmap).

Worried about security or privacy? SQL Auto Import is open-source, so you can [view the source code](https://github.com/kevinlakhani/sqlautoimport/blob/master/sqlautoimport.py) to investigate any concerns. If you find an issue, report it [here](https://github.com/kevinlakhani/sqlautoimport/issues)!

# Downloads

## Windows

64-bit Download: [v2.0.0 Portable 64-bit executable file (.exe)](https://github.com/kevinlakhani/sqlautoimport/raw/master/sqlautoimport.exe)

32-bit Download: [v2.0.0 Portable 32-bit executable file (.exe)](https://github.com/kevinlakhani/sqlautoimport/raw/master/sqlautoimport-32.exe)

## macOS, Linux, and others
In progress. 

For now, use [sqlautoimport.py](https://github.com/kevinlakhani/sqlautoimport/blob/master/sqlautoimport.py) with Python. 

Dependencies listed in [requirements.txt](https://github.com/kevinlakhani/sqlautoimport/blob/master/requirements.txt) will also need to be installed.

# Usage
Open Command Prompt in the directory your copy of `sqlautoimport.exe` (or `sqlautoimport-32.exe`) is located. Alternatively, you can point the Command Prompt to the full directory path where your executable is located.

For regular usage, you must specify the `FLAVOR`, `HOST`, `PORT`, `DATABASE`, `USERNAME`, and `PASSWORD` to connect to. 

Current supported `FLAVOR` choices are:

`postgresql`, `mysql`, `sqlite` ,`oracle`, and `mssql`

These correspond to:

[PostgreSQL](https://www.postgresql.org/), [MySQL](https://www.mysql.com/), [SQLite](https://sqlite.org), [Oracle](https://oracle.com), and [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/default.aspx). 

More flavor compatibility is coming soon.

You will probably also want to include the `DIRECTORY` where your files are located, but if you don't it will be assumed that the local directory contains the files you want to import to your database. 

Here's an example command:
```
sqlautoimport.exe --directory "C:\My Files" --flavor mysql --host my.host.com --port 3306 --database db --username u --password p
```

Additionally, be sure to use the `--schema` argument if you need to load files into a schema in your database other than its default schema.

While SQL Auto Import expects a comma-delimited, CSV (`.csv`) file by default, you can specify a different file extension through the `--extension` argument. If your files are not comma-delimited, you will also need to use the `--delimiter`argument. For example, for tab-separated files use `--delimiter \t`. For pipe-delimited files, use `--delimiter |`.

There are additional arguments to help with flexibility and automation needs, such as `-s` and `-y`. For more information, use the `--help` argument. Its full output is shown below for your convenience:
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
	 - [ ] Support for specifying modes other than `replace` (e.g. `append`)
	 - [ ] Support for `.json` files
	 - [ ] `--prefix` and `--suffix` options to prepend/append to table names
	 - [ ] Option to recursively search for files in `DIRECTORY`
	 - [x] ~~Support for schema specification~~
	 - [ ] Performance tuning: specify chunk size and/or auto-select settings based on data size
 - [ ] macOS and Linux bundles
 - [ ] Automated unit and functional tests
 - [ ] Support for Redshift, Presto and [other "external" dialects](https://docs.sqlalchemy.org/en/13/dialects/#external-dialects)
 - [ ] Override default column type settings (e.g. specify a column as `money` instead of `double` or `smallint` instead of `bigint`)
 - [ ] Web GUI

# 

"Python" is a registered trademark of the [Python Software Foundation]([https://www.python.org/psf/)
