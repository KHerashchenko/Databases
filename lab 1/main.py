import psycopg2
import csv, re
import pandas as pd
from datetime import datetime
from os.path import isfile, join
from os import listdir

table_name = 'zno_results'

def create_table(cursor, conn):
    with open('DATA/Odata2019File.csv', encoding="windows-1251") as f:
        data = csv.DictReader(f, delimiter=';')
        colnames = data.fieldnames

    query = "CREATE TABLE IF NOT EXISTS {} ( \n".format(table_name, table_name)

    for column in colnames:
        if (column in ('Birth') or 'Ball' in column):
            query += column + " real,\n"
        elif (column in ('EONAME', 'EOParent') or 'PTName' in column):
            query += column + " TEXT,\n"
        else:
            query += column + " VARCHAR(128),\n"

    query = query[:-2] + ",\nYear smallint);"

    with open('SQL/create_table_query.sql', 'w') as f:
        f.write(query)

    cursor.execute(query)
    conn.commit()
    colnames.append('Year')
    return colnames

def create_audit_table(file_pathes, cursor, conn):

    query = """ CREATE TABLE IF NOT EXISTS audit ( \n
            filename VARCHAR(256) PRIMARY KEY,\n
            status VARCHAR(128),
            execution_time REAL
        );
        """
    cursor.execute(query)

    for path in file_pathes:
        query = """INSERT INTO audit VALUES ('{}','waiting',{}) 
                ON CONFLICT (filename) DO NOTHING;""".format(path, 'NULL')
        cursor.execute(query)

    with open('SQL/create_audit_table_query.sql', 'w') as f:
        f.write(query)

    conn.commit()

def recode_file(csv_file_path):
    # changing file encoding
    year = int(re.findall(r'\d+', csv_file_path)[0])
    with open(csv_file_path, encoding="windows-1251") as f:
        data = csv.DictReader(f, delimiter=';')

        i = 0
        with open('DATA/{}_encoded.csv'.format(csv_file_path[5:-4]), 'w', encoding='utf8') as f_new:
            for row in data:
                i += 1
                for key in row.keys():
                    if row[key] == 'null':
                        row[key] = 'NULL'
                    elif not (key in ('Birth') or 'Ball' in key):
                        row[key] = "'" + row[key].replace("'", "`") + "'"
                    else:
                        row[key] = row[key].replace(',', '.')
                row_values = '' + ";".join(row.values())

                f_new.write(row_values + ';{}\n'.format(year))
                if i % 100000 == 0: print('Writed {} rows to file DATA/{}_encoded.csv'.format(i, csv_file_path[5:-4]))
            print('File DATA/{}_encoded.csv is ready'.format(csv_file_path[5:-4]))
    return 'DATA/{}_encoded.csv'.format(csv_file_path[5:-4])

def split_file(csv_file_path):

    with open(csv_file_path, encoding="utf8") as f:

        lines_per_file = 100000
        smallfile = None
        file_names = []

        for lineno, line in enumerate(f):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = '{}_{}.csv'.format(csv_file_path[:-4], lineno + lines_per_file)
                file_names.append(small_filename)
                smallfile = open(small_filename, "w", encoding='utf8')
            smallfile.write(line)
        if smallfile:
            smallfile.close()

    print('File {} splited into {}'.format(csv_file_path, ','.join(file_names)))
    return file_names

def prepare_data(csv_file_path):
    encoded_file_path = recode_file(csv_file_path)
    file_pathes = split_file(encoded_file_path)

    return file_pathes

def insert_data(file_pathes, cursor, conn, cols):

    for path in file_pathes:

        try:
            data = pd.read_csv(path, names=cols, delimiter=';', low_memory=False)

            query = ''
            start_time = datetime.now()
            for idx, row in data.head(1).iterrows():
                query += "INSERT INTO {} VALUES ({});\n".format(table_name, ','.join(row.map(str)).replace('nan', 'NULL'))
                cursor.execute(query)

            timediff = (datetime.now() - start_time).microseconds
            query = """INSERT INTO audit VALUES ('{}','copied',{}) 
                ON CONFLICT (filename) DO 
                UPDATE SET status = EXCLUDED.status, execution_time = EXCLUDED.execution_time;""".format(path, timediff)
            cursor.execute(query)

            conn.commit()
            print('Successfuly inserted file ' + path)
        except Exception as error:
            print("Something went wrong with inserting {}: {}".format(path, error))
            conn.rollback()

            query = """INSERT INTO audit VALUES ('{}','failed',{}) 
                ON CONFLICT (filename) DO 
                UPDATE SET status = EXCLUDED.status, execution_time = EXCLUDED.execution_time;""".format(path, 'NULL')
            cursor.execute(query)
            conn.commit()

        # query = "COPY zno_results ({}) FROM '/csv/{}' WITH DELIMITER ';' NULL AS 'NULL' CSV;".format(','.join(cols), path[5:])

def custom_query(cursor):

    query = open('SQL/custom_query.sql', encoding='utf8')
    cursor.execute(query.read())
    data = cursor.fetchall()

    file_result = 'DATA/custom_query_result.txt'
    with open(file_result, 'w') as f:
        f.write('\n'.join(['Best grade for Eng test in %s is %s' % (i,j) for (i, j) in data]))

    return file_result

def main():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="192.168.99.100"
        )

        conn.autocommit = True
        cursor = conn.cursor()

        cols = create_table(cursor, conn)
        print('{} table created'.format(table_name))
        csv_file_pathes = ['DATA/Odata2019File.csv', 'DATA/Odata2020File.csv']

        print('Preparing files')
        all_pathes = []
        for path in csv_file_pathes:
            # file_pathes = prepare_data(path)

            file_pathes = ['DATA/'+f for f in listdir('DATA/')
                           if isfile(join('DATA/', f))
                                and 'encoded_' in f
                                and re.findall(r'\d+', path)[0] in f]

            all_pathes.append(file_pathes)

        all_pathes = [item for sublist in all_pathes for item in sublist]

        create_audit_table(all_pathes, cursor, conn)
        print('Audit table created')

        cursor.execute("SELECT * FROM audit where status != 'copied';")
        waiting_files = [item[0] for item in cursor.fetchall()]
        if waiting_files:
            print('Not copied files detected:', ', '.join(waiting_files))
            insert_data(waiting_files, cursor, conn, cols)
        else:
            print('All files successfuly inserted')

        file_result = custom_query(cursor)
        print('Custom query result is stored in %s' % file_result)
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    main()