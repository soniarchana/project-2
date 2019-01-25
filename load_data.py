import pandas as pd
import sqlite3
import os

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect



# Function to load data from csv file to sqlite tables
def load_from_csv_to_sqlite_tables(data_files, table_names, engine):
    """Return True if load csv data to sqlite successfully"""

    return_value = True
    
    for i in range(0, len(data_files)):

        # Read the csv files into Panda dataframe
        df = pd.read_csv(data_files[i])

        # Create index for the df
        df.insert(0, 'ID', range(0, len(df)))
        df.set_index('ID', inplace=True)

        # Remove the space from the data in dataframes, and convert "…" to "0" if needed
        if i not in [3, 4, 8]: # data in these three files do not need to be cleaned
            if i in [0, 1, 2]:
                column_range = range(2, len(df.columns)) # Start with 3rd column
            else:
                column_range = range(3, len(df.columns)) # Start with 4th column

            # Remove space, replace "…" with "0", then convert to integer
            for j in column_range:
                df.iloc[:, j] = [int(x.replace(" ", "").replace("…", "0")) for x in df.iloc[:, j]]

        # Create tables in sqlite from the dataframes
        table_name = table_names[i]
        try: 
            df.to_sql(table_name, engine, if_exists='replace')
            print(f"Table, {table_name}, has been created successfully")
        except Exception as e:
            print(f"Table, {table_name}, can not be created")
            print(e)
            print("----------") 
            return_value = False
    return return_value



# Code below is for adding primary keys to the tables in sqlite. 
# As alter table to add pk does not work for SQLite, 
# need to create new tables with PK, then load data from the tables created above to the new tables.
# drop the tables created above

# Generate create table statement for table_names 0,1,2
def create_table_0_1_2(new_table_name):
    """Return create table statement for table_names with index 0, 1, 2"""

    create_table = f"CREATE TABLE IF NOT EXISTS {new_table_name} (\
    ID BIGINT PRIMARY KEY,\
    region_subregion_country_area TEXT,\
    country_code BIGINT,\
    '1950' BIGINT, '1951' BIGINT, '1952' BIGINT,\
    '1953' BIGINT, '1954' BIGINT, '1955' BIGINT,\
    '1956' BIGINT, '1957' BIGINT, '1958' BIGINT,\
    '1959' BIGINT, '1960' BIGINT, '1961' BIGINT,\
    '1962' BIGINT, '1963' BIGINT, '1964' BIGINT,\
    '1965' BIGINT, '1966' BIGINT, '1967' BIGINT,\
    '1968' BIGINT, '1969' BIGINT, '1970' BIGINT,\
    '1971' BIGINT, '1972' BIGINT, '1973' BIGINT,\
    '1974' BIGINT, '1975' BIGINT, '1976' BIGINT,\
    '1977' BIGINT, '1978' BIGINT, '1979' BIGINT,\
    '1980' BIGINT, '1981' BIGINT, '1982' BIGINT,\
    '1983' BIGINT, '1984' BIGINT, '1985' BIGINT,\
    '1986' BIGINT, '1987' BIGINT, '1988' BIGINT,\
    '1989' BIGINT, '1990' BIGINT, '1991' BIGINT,\
    '1992' BIGINT, '1993' BIGINT, '1994' BIGINT,\
    '1995' BIGINT, '1996' BIGINT, '1997' BIGINT,\
    '1998' BIGINT, '1999' BIGINT, '2000' BIGINT,\
    '2001' BIGINT, '2002' BIGINT, '2003' BIGINT,\
    '2004' BIGINT, '2005' BIGINT, '2006' BIGINT,\
    '2007' BIGINT, '2008' BIGINT, '2009' BIGINT,\
    '2010' BIGINT, '2011' BIGINT, '2012' BIGINT,\
    '2013' BIGINT, '2014' BIGINT, '2015' BIGINT);"
    return create_table


# Generate create table statement for table_names 3
def create_table_3(new_table_name):
    """Return create table statement for table_names with index 3"""

    create_table = f"CREATE TABLE IF NOT EXISTS {new_table_name} (\
    ID BIGINT PRIMARY KEY,\
    region_subregion_country_area TEXT,\
    country_code BIGINT,\
    '1950' FLOAT, '1955' FLOAT,\
    '1960' FLOAT, '1965' FLOAT,\
    '1970' FLOAT, '1975' FLOAT,\
    '1980' FLOAT, '1985' FLOAT,\
    '1990' FLOAT, '1995' FLOAT,\
    '2000' FLOAT, '2005' FLOAT,\
    '2010' FLOAT, '2015' FLOAT);"
    return create_table


# Function to create table for table_names 4
def create_table_4(new_table_name):
    """Return create table statement for table_names with index 4"""

    create_table = f"CREATE TABLE IF NOT EXISTS {new_table_name} (\
    ID BIGINT PRIMARY KEY,\
    region_subregion_country_area TEXT,\
    country_code BIGINT,\
    '1950-1955' FLOAT, '1955-1960' FLOAT,\
    '1960-1965' FLOAT, '1965-1970' FLOAT,\
    '1970-1975' FLOAT, '1975-1980' FLOAT,\
    '1980-1985' FLOAT, '1985-1990' FLOAT,\
    '1990-1995' FLOAT, '1995-2000' FLOAT,\
    '2000-2005' FLOAT, '2005-2010' FLOAT,\
    '2010-2015' FLOAT);"
    return create_table


# Function to create table for table_names 5,6,7
def create_table_5_6_7(new_table_name):
    """Return create table statement for table_names with index 5, 6, 7"""

    create_table = f"CREATE TABLE IF NOT EXISTS {new_table_name} (\
    ID BIGINT PRIMARY KEY,\
    region_subregion_country_area TEXT,\
    country_code BIGINT,\
    reference_date BIGINT,\
    '0-4' BIGINT, '5-9' BIGINT, '10-14' BIGINT,\
    '15-19' BIGINT, '20-24' BIGINT, '25-29' BIGINT,\
    '30-34' BIGINT, '35-39' BIGINT, '40-44' BIGINT,\
    '45-49' BIGINT, '50-54' BIGINT, '55-59' BIGINT,\
    '60-64' BIGINT, '65-69' BIGINT, '70-74' BIGINT,\
    '75-79' BIGINT, '80+' BIGINT, '80-84' BIGINT,\
    '85-89' BIGINT, '90-94' BIGINT, '95-99' BIGINT, '100+');"
    return create_table
    

# Function to create table for table_names 8
def create_table_8(new_table_name):
    """Return create table statement for table_names with index 8"""

    create_table = f"CREATE TABLE IF NOT EXISTS {new_table_name} (\
    ID BIGINT PRIMARY KEY,\
    country TEXT,\
    code TEXT,\
    country_code BIGINT,\
    continent TEXT,\
    capital TEXT,\
    latitude FLOAT,\
    longitude FLOAT);"
    return create_table


# Create insert statement
def insert_data(table_name, new_table_name):
    """Return insert data statement"""

    insert_data = f"INSERT INTO {new_table_name} SELECT * FROM {table_name};"
    return insert_data


# Create drop table statement
def drop_table(table_name):
    """Return drop table statement"""

    drop_table = f"DROP TABLE {table_name};"
    return drop_table


# Function to drop tables
def drop_tables(table_names, cur):
    """Return True if drop tables successful"""

    return_value = True
    try: 
        cur.execute("begin")
        for i in range(0, len(table_names)):
            table_name = table_names[i]
            new_table_name = f"{table_name}_new"
            cur.execute(drop_table(table_name))
        cur.execute("commit")
        print(f"drop tables successful")
    except Exception as e:
        print(f"can not drop table")
        print(e)
        print("----------") 
        return_value = False
        
    return  return_value 
    

# Function to create new tablea with pk and insert data
def create_sqlite_tables_with_pk(orig_table_names, new_table_names, cur):
    """Return True if create sqlite tables with PK and load data successful"""

    return_value = True
    for i in range(0, len(new_table_names)):
        orig_table_name = orig_table_names[i]
        new_table_name = new_table_names[i]

        try:
            cur.execute("begin")
            if i in [0,1,2]:
                cur.execute(create_table_0_1_2(new_table_name))
            elif i == 3:
                cur.execute(create_table_3(new_table_name))
            elif i == 4:
                cur.execute(create_table_4(new_table_name))
            elif i == 8:
                cur.execute(create_table_8(new_table_name))
            else:
                cur.execute(create_table_5_6_7(new_table_name))
            cur.execute(insert_data(orig_table_name, new_table_name))      
            cur.execute("commit")
            print(f"Table, {new_table_name}, Primary key added successpully")
        except Exception as e:
            print(f"Table, {new_table_name}, Can not add primary key")
            print(e)
            print("----------")  
            return_value = False
    return return_value


def load_to_sqlite():
    """Execute the functions to load data to sqlite and create PK for the tables"""

    db_url = 'sqlite:///./db/world_population.sqlite'

    data_files = [
           'data/TOTAL_POPULATION_BOTH_SEXES.csv',
           'data/TOTAL_POPULATION_FEMALE.csv',
           'data/TOTAL_POPULATION_MALE.csv',
           'data/SEX_RATIO_OF_TOTAL_POPULATION.csv',
           'data/POPULATION_GROWTH_RATE.csv',
           'data/POPULATION_BY_AGE_MALE.csv',
           'data/POPULATION_BY_AGE_FEMALE.csv',
           'data/POPULATION_BY_AGE_BOTH_SEXES.csv',
           'data/country_continent.csv']  

    new_table_names = [
        'total_population_both_sexes',
        'total_population_female',
        'total_population_male',
        'sex_ratio_of_total_population',
        'population_growth_rate',
        'population_by_age_male',
        'population_by_age_female',
        'population_by_age_both_sexes',
        'country_continent']

    orig_table_names = [
        'total_population_both_sexes_o',
        'total_population_female_o',
        'total_population_male_o',
        'sex_ratio_of_total_population_o',
        'population_growth_rate_o',
        'population_by_age_male_o',
        'population_by_age_female_o',
        'population_by_age_both_sexes_o',
        'country_continent_o']

    print("Start: remove existing db file, world_population.sqlite")
    db_file = 'db/world_population.sqlite'
    if os.path.exists(db_file):
        os.remove(db_file)
    print("End: remove existing db file")
    print("")

    print("Start: create engine")
    db_url = 'sqlite:///./db/world_population.sqlite'
    engine = create_engine(db_url)
    print("End: create engine")
    print("")

    ### Load data from csv file into sqlite tables
    print("Start: load from CSV to SQLite")
    load_from_csv_to_sqlite_tables(data_files, orig_table_names, engine)
    print("End: load from CSV to SQLite")
    print("")
        
    ### Add Primary Key to the tables in sqlite
    #connect to the database
    print("Start: connect to SQLite, create cursor")
    conn = sqlite3.connect('db/world_population.sqlite') 
    conn.isolation_level = None
    cur = conn.cursor()
    print("End: connect to SQLite and create cursor")
    print("")
        
    print("Start: create new tables with PK, load data to the new tables from original tables")
    create_sqlite_tables_with_pk(orig_table_names, new_table_names, cur)
    print("End: create new tables with PK...")
    print("")
        
    print("Start: drop original tables")
    drop_tables(orig_table_names, cur)
    print("End: drop original tables")
    print("")
        
    print("Starting: close cursor, close SQLite Connection")
    cur.close()
    conn.close()
    print("End: close cursor, close SQLite Connection")
    print("Finished Loading data")
    print("")
