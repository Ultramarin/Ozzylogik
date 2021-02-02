from config import *
from task_1 import *
from task_2 import *


if __name__ == '__main__':
    print(f"""
    1 - task Сгенерировать csv файл из 1024 записей по 6 столбцов, заполненных строками случайных символов (цифры и латинские буквы) длиной по 8 символов. 
    B. Считать содержимое файла, заменить нечетные цифры символом #, удалить записи, в которых любая из шести строк начинается с гласной буквы, сохранить отредактированный файл с другим именем. 
    """
          )
    generator_csv(name_file=FILE_NAME, column=COLUMN, line=LINE, count_symbol=COUNT_SYMBOL)
    reader(file_name=FILE_NAME, new_file_name=NEW_FILE_NAME)
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
#         print(f"result")
#         for row in result:
#             print(result)
#