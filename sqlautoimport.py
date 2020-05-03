print("Loading prerequisites...")
import pandas, sqlalchemy, tqdm, os, time, json, sys
# https://docs.sqlalchemy.org/en/13/dialects/
import psycopg2, sqlite3, cx_Oracle, pyodbc, MySQLdb
print()

def chunker(seq, size):
    # Thanks to miraculixx
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

config_path, csv_path = 'config.json',''
if len(sys.argv) > 1:
    config_path = sys.argv[1] 
    if len(sys.argv) > 2:
        csv_path = sys.argv[2]

print('''
    Welcome to the SQL Auto Import tool. This tool
    allows you to quickly create/populate or replace 
    tables in a SQL database with CSV files.

    PostreSQL, MySQL, SQLite, MSSQL, and Oracle dialects
    are supported.

    This tool will attempt to load connection settings
    from a config.json file by default. You can specify
    a file to use as a command line argument. If no file
    is found or if there is an issue, you will be asked
    to input the information below. You will have the 
    options to save the connection settings. 

    Additionally, you will need to specify a directory 
    path to your CSV files (e.g. C:\MyFiles). You can
    also pass this in as a second command-line argument. 
    
    If you do not enter a path, the local directory will 
    be used.

    This tool will use the names of your files as table 
    names (in lowercase), so make sure they're correct. 
    If a table already exists, it will be replaced.

    Only the default schema is currently supported.
'''
)

dialect, host, port, database, password = ('' for i in range(5))

settings = {'dialect': '', 'host': '', 'database': '', 'port': '', 'username': '', 'password': ''}
try:
    with open(config_path) as config_file:
        config = json.load(config_file)

    settings['dialect'] = config['dialect']
    settings['host'] = config['host']
    settings['port'] = config['port']
    settings['database'] = config['database']
    settings['username'] = config['username']
    settings['password'] = config['password']
except Exception as e:
    print ('No config.json file found or there was an issue loading the configuration.')
    print(e)
    print()

if any(settings[x] == '' for x in settings.keys()):
    print('Please enter the SQL connection settings prompted below.')
    for x in settings.keys():
        print()
        hint = ''
        if x == 'dialect':
            hint = ' (e.g. postgres, mysql, mssql, oracle)'
        if x == 'port':
            hint = ' (usually 5432 for postgres or 3306 for mysql)'
        if settings[x] == '':
            settings[x] = input(f'{x.capitalize()}{hint}: ')
    print()
    save = input('Would you like to save these settings for next time [y/n]? ').lower()
    if save in ['y','yes']:
        new_config = '{\n'
        for k,v in settings.items():
            new_config += f'\t"{k}":"{v}"'
            if k != list(settings.keys())[-1]: 
                new_config += ','
            new_config += '\n'
        new_config += '}'

        with open('config.json','w') as config_file:
            config_file.write(new_config)
            print('config.json saved succefully')
            print()
dialect = ''
if settings['dialect'].lower() in ['postgres','postgresql']:
    dialect = 'postgres'
elif settings['dialect'].lower() == 'mysql':
    dialect = 'mysql+mysqldb'
elif settings['dialect'].lower() == 'sqlite':
    dialect = 'sqlite+pysqlite'
elif settings['dialect'].lower() == 'oracle':
    dialect = 'oracle+cx_oracle'
elif settings['dialect'].lower() == 'mssql':
    dialect = 'mssql+pyodbc'


uri = f"{dialect}://{settings['username']}:{settings['password']}@{settings['host']}:{settings['port']}/{settings['database']}"
print()
print('The following connection URI will be used:')
print(uri)
print()
engine = sqlalchemy.create_engine(uri)

if csv_path == '':
    csv_path = input('Directory Path: ')

csv_files,file_list = [],[]

if csv_path == '':
    file_list = os.listdir()
else:
    file_list = os.listdir(csv_path)

for f in file_list:
    if f.endswith(".csv"):
        csv_files.append(f)

#test = pandas.read_sql('select * from baseline_cognitive_data', engine)
#print(test)
if len(csv_files) > 0:
    confirm = input(f'''
This will import {str(len(csv_files))} file(s) into the specified database. 
Any tables that already exists will be overwritten.
Continue? [y/n]: '''
    ).lower()
    if confirm in ['y','yes']:
        for x in range(0,len(csv_files)):
            print()
            print(f'Reading {str(csv_files[x])}...')
            df = None
            try:
                df = pandas.read_csv(os.path.join(csv_path,csv_files[x]))
            except Exception as e:
                print(f'Error reading file: {str(csv_files[x])}')
                print(e)

            try:    
                print(f"Importing {str(csv_files[x])} to database as {csv_files[x][:csv_files[x].index('.csv')].lower()}...")
                print(f'Rows to insert: {(len(df.index))}')
                
                start = time.perf_counter()
                block = int(len(df) / 10)
                with tqdm.tqdm(total=len(df)) as progress:
                    for i, cdf in enumerate(chunker(df, block)):
                        mode = "replace" if i == 0 else "append"
                        cdf.to_sql(
                            csv_files[x][:csv_files[x].index('.csv')].lower(),
                            engine,
                            index = False,
                            if_exists = mode,
                            # schema = 'default', #TO DO: arguments and/or settings file
                            method = 'multi', 
                            chunksize = 10000
                            )            
                        progress.update(block)
                        tqdm.tqdm._instances.clear()

                finish = time.perf_counter()
                print(f'''Completed importing {str(x+1)} out of {len(csv_files)} file(s).
Total time: {finish - start:0.4f} seconds.
Seconds per row: {(finish - start)/(len(df.index)):0.4f}
''')
            except Exception as e:
                print(e)
        print()
        print('Finished!')
else:
    print('No CSV files found in the specified directory.')

print()
input('Press any key to exit.')