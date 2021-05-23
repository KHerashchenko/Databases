from pymongo import MongoClient
import logging
import csv
import re
from datetime import datetime

from constants import DB_URL, DATA_PATHES

def get_user_query(collection, logger):
    """
    Порівняти середній бал з Історії України у кожному регіоні у 2020 та 2019 роках 
    серед тих кому було зараховано тест
    """
    start_time = datetime.now()
    query = list(collection.aggregate(
        [
            {"$match": {"histTestStatus": "Зараховано"}},
            {"$group": {"_id": {"Year": "$Year", "Region": "$histPTRegName"},
                        "avg": {"$avg": "$histBall100"}}},
        ]
    ))
    with open("result.csv", "w") as f:

        writer = csv.DictWriter(f, fieldnames=["_id", "avg"])
        writer.writeheader()

        for row in query:
            writer.writerow(row)

    exec_time = (datetime.now() - start_time).seconds

    logger.info(f'Writing query results to file completed in {exec_time} secs')


def insert_data(collection, audit, data_path, last_row_number, logger, rows_to_write = 1000):

    with open(data_path, encoding="windows-1251") as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter=";")

        year = int(re.findall(r'\d+', data_path)[0])

        arr = []
        start_time = datetime.now()

        for i, row in enumerate(csv_reader):

            if i <= last_row_number:
                continue

            row["Year"] = year
            for field in row.keys():
                if "Ball" in field:
                    try:
                        row[field] = float(row[field])
                    except ValueError:
                        if row[field] != 'null':
                            row[field] = float(row[field].replace(',', '.'))
                        else:
                            row[field] = None
            arr.append(row)

            if i % rows_to_write == 0:

                try:
                    collection.insert_many(arr)
                    logger.info(f'Populating Zno_data Collection with {rows_to_write} rows')
                    now = datetime.now()
                    logger.info('Updating Audit Collection')
                    audit.update_one({"file_path": data_path},
                                     {"$set": {"last_row": i},
                                      "$inc": {"execution_time": (now - start_time).seconds}})
                    print(data_path, i)
                    arr = []
                except Exception as e:
                    logger.info(f'Something went wrong: {e}')
                    raise Exception
                start_time = datetime.now()

        try:
            collection.insert_many(arr)

            logger.info(f'Populating Zno_data Collection with {rows_to_write} rows')
            now = datetime.now()
            logger.info('Updating Audit Collection')

            audit.update_one({"file_path": data_path},
                             {"$set": {"last_row": i, "status": "complete"},
                              "$inc": {"execution_time": (now - start_time).seconds}})
            print(data_path, i)
        except Exception as e:
            logger.info(f'Something went wrong: {e}')
            raise Exception

    logger.info(f'Inserting from {data_path} is finished')


def main():

    start_prog_time = datetime.now()

    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="logs.txt", format="%(asctime)s: %(message)s", level=logging.INFO)
    logger.info("Connecting to db")

    try:
        client = MongoClient(DB_URL)
    except Exception as e:
        logger.info(f'Connecting to db failed')
        raise Exception

    db = client.zno_results

    collection = db.zno_data
    audit = db.audit

    logger.info('Populating Audit Collection')

    if 'audit' not in db.list_collection_names():
        for path in DATA_PATHES:
            audit.insert_one({"file_path": path, "last_row": 0, "execution_time": 0, "status": "incomplete"})

    for path in DATA_PATHES:
        audit_info = audit.find_one({"file_path": path})
        status = audit_info["status"]
        row_number = audit_info["last_row"]

        if status == "incomplete":
            logger.info(f'Populating Zno_data Collection with file {path}')

            insert_data(collection, audit, path, row_number, logger)

    get_user_query(collection, logger)

    exec_prog_time = (datetime.now() - start_prog_time).seconds

    logger.info(f"Program finished in {exec_prog_time} secs")

if __name__ == "__main__":
    main()