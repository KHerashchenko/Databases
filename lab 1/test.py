import psycopg2, csv, re

table_name = 'zno_results'

def create_table(cursor):
    with open('DATA/Odata2019File.csv', encoding="windows-1251") as f:
        data = csv.DictReader(f, delimiter=';')
        colnames = data.fieldnames

    query = "DROP TABLE {}; CREATE TABLE {} ( \nYear  SMALLINT,\n".format(table_name, table_name)

    for column in colnames:
        if (column in ('Birth') or 'Ball' in column):
            query += column + " SMALLINT,\n"
        elif (column in ('EONAME', 'EOParent') or 'PTName' in column):
            query += column + " VARCHAR(256),\n"
        else:
            query += column + " VARCHAR(128),\n"

    query = query[:-2] + ");"

    with open('SQL/create_table_query.sql', 'w') as f:
        f.write(query)

    cursor.execute(query)


def insert_data(csv_file_path, cursor):
    year = re.findall(r'\d+', csv_file_path)[0]

    with open(csv_file_path, encoding="windows-1251") as f:
        data = csv.DictReader(f, delimiter=';')

        for row in data:
            for key in row.keys():
                if row[key] == 'null':
                    row[key] = 'NULL'
                elif not(key in ('Birth') or 'Ball' in key):
                    row[key] = "'" + row[key].replace("'", "`") + "'"
                else:
                    row[key] = row[key].replace(',', '.')

            row_values = year + ", " + ", ".join(row.values())
            query = "BEGIN; INSERT INTO {} VALUES ({}); COMMIT;".format(table_name, row_values)

            try:
                cursor.execute(query)
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

            break


    # write last query in a file as example
    with open('SQL/insert_values_query.sql', 'w') as f:
        f.write(query)

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

        create_table(cursor)

        csv_file_path = 'DATA/Odata2019File.csv'
        insert_data(csv_file_path, cursor)

        csv_file_path = 'DATA/Odata2020File.csv'
        insert_data(csv_file_path, cursor)

        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    main()
