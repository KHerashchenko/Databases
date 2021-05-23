# Databases Labs - Геращенко Катерина

## Lab 1

Для начала работы нужно загрузить в папку `DATA` [файлы с результатами ЗНО](https://zno.testportal.com.ua/opendata) за несколько лет.   
Далее в корне проекта выполнить команду `docker-compose up`  

Файл `main.py` выполняет операции по созданию в базе данных таблиц, их заполнению, а также выполнению индивидуального задания.  
*Задание:* Порівняти найкращий бал з Англійської мови у 2020 та 2019 роках серед тихкому було зараховано тест  
Результат запроса будет сохранен в файле `DATA/custom_query_result.txt`  

Нормальный флоу программы сопровождается *выводом в консоль* следующих сообщений:

```
zno_results table created
Preparing files
Writed 100000 rows to file DATA/Odata2019File_encoded.csv
Writed 200000 rows to file DATA/Odata2019File_encoded.csv
Writed 300000 rows to file DATA/Odata2019File_encoded.csv
File DATA/Odata2019File_encoded.csv is ready
File DATA/Odata2019File_encoded.csv splited into DATA/Odata2019File_encoded_100000.csv,DATA/Odata2019File_encoded_200000.csv,DATA/Odata2019File_encoded_300000.csv,DATA/Odata2019File_encoded_400000.csv
Writed 100000 rows to file DATA/Odata2020File_encoded.csv
Writed 200000 rows to file DATA/Odata2020File_encoded.csv
Writed 300000 rows to file DATA/Odata2020File_encoded.csv
File DATA/Odata2020File_encoded.csv is ready
File DATA/Odata2020File_encoded.csv splited into DATA/Odata2020File_encoded_100000.csv,DATA/Odata2020File_encoded_200000.csv,DATA/Odata2020File_encoded_300000.csv,DATA/Odata2020File_encoded_400000.csv
Audit table created
Not copied files detected: DATA/Odata2019File_encoded_100000.csv, DATA/Odata2019File_encoded_200000.csv, DATA/Odata2019File_encoded_300000.csv, DATA/Odata2019File_encoded_400000.csv, DATA/Odata2020File_encoded_100000.csv, DATA/Odata2020File_encoded_200000.csv, DATA/Odata2020File_encoded_300000.csv, DATA/Odata2020File_encoded_400000.csv
Successfuly inserted file DATA/Odata2019File_encoded_100000.csv
Successfuly inserted file DATA/Odata2019File_encoded_200000.csv
Successfuly inserted file DATA/Odata2019File_encoded_300000.csv
Successfuly inserted file DATA/Odata2019File_encoded_400000.csv
Successfuly inserted file DATA/Odata2020File_encoded_100000.csv
Successfuly inserted file DATA/Odata2020File_encoded_200000.csv
Successfuly inserted file DATA/Odata2020File_encoded_300000.csv
Successfuly inserted file DATA/Odata2020File_encoded_400000.csv
Custom query result is stored in DATA/custom_query_result.txt
```  

Данные о времени транзакций содержатся в таблице `audit` в поле `execution_time`

---
## Lab 2

Для старта сервисов pgadmin4 и postgres требуется выполнить команду `docker-compose up`. Далее можно повторить действия из первой лабораторной работы, чтобы заполнить бд данными.  
Далее проводим миграции с помощью имеджа flyway.
```
docker-compose -f migrate.yaml up
```

Результат выполнения заносится в дефолтную таблицу с версиями миграций.

![Logical model](https://github.com/KHerashchenko/Databases/blob/master/lab%202/logical.png)

![Physical model](https://github.com/KHerashchenko/Databases/blob/master/lab%202/physical.png)

---
## Lab 4

Для начала работы нужно загрузить в папку `DATA` [файлы с результатами ЗНО](https://zno.testportal.com.ua/opendata) за несколько лет.

Файл `main.py` выполняет операции по созданию в базе данных коллекций, их заполнению, а также выполнению индивидуального задания.  
*Задание:* Порівняти середній бал з Історії України у кожному регіоні у 2020 та 2019 роках серед тих кому було зараховано тест  
Результат запроса будет сохранен в файле `result.csv`  

Нормальный флоу программы сопровождается *логированием* в файл `logs.txt`
