import csv
import mysql.connector
from mysql.connector import Error


HOST_NAME = "localhost"
USER = "legio"
PASS_MYSQL = "YOUR_PASSWD"
TABLE = "TEST"
DB = "TEST"
FILE_NAME = "test.csv"


def create_connection_sql_server(
        host_name: str,
        user_name: str,
        user_password: str,
):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def create_connection_db(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error:
        print(f"The error '{Error}' occurred")


def create_sq_table(connect):
    create_users_table = """
    CREATE TABLE IF NOT EXISTS TEST (
      id INT AUTO_INCREMENT, 
      column0 TEXT , 
      column1 TEXT, 
      column2 TEXT, 
      column3 TEXT, 
      column4 TEXT,
      column5 TEXT,  
      PRIMARY KEY (id)
    ) ENGINE = InnoDB
    """

    execute_query(connect, create_users_table)


def insert_value_file_mysql(
        connect,
        file_name: str = FILE_NAME,
        table: str = TABLE,
):
    """
    Insertvalue in MYSql with file
    :param file_name:
    :return:
    """
    insert_query = f"""INSERT INTO
      {table} (column0, column1, column2, column3,column4,column5)
    VALUES """
    with open(file_name, newline='') as file:
        spam_reader = csv.reader(file, delimiter=',', quotechar='|')
        temp_s = ""
        for row in spam_reader:
            temp_s += "(" + ",".join(map(lambda x: f"'{x}'", row)) + "),"
        insert_query += f"{temp_s[:-1]} ;"
    execute_query(connect, insert_query)


def delete_value_mysql(
        connect: object,
        table: str = TABLE
):
    delete_query = f"DELETE FROM {table} WHERE column1 REGEXP '^[0-9].*';"
    execute_query(connect, delete_query)


def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}'")


if __name__ == '__main__':
    print(f"""
       Считать содержимое файла из пункта А, создать программно базу данных mysql, сохранить все данные в таблицу. 
       Средствами sql удалить записи, в которых во втором столбце первый символ цифра.
       """
          )
    connection = create_connection_sql_server(
        host_name=HOST_NAME,
        user_name=USER,
        user_password=PASS_MYSQL)
    create_database_query = f"CREATE DATABASE {DB}"
    create_database(connection, create_database_query)
    connect = create_connection_db(
        host_name=HOST_NAME,
        user_name=USER,
        user_password=PASS_MYSQL,
        database=DB

    )
    if connect:
        create_sq_table(connect)
        insert_value_file_mysql(connect)
        delete_value_mysql(connect)
        result = execute_read_query(connect, f'SELECT * from {TABLE};')
        # print(f"result")
        # for row in result:
        #     print(result)
