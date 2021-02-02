import csv
import random
import string
from typing import Union

COUNT_SYMBOL = 8
COLUMN = 6
LINE = 1024
FILE_NAME = "test.csv"
NEW_FILE_NAME = "new_test.csv"


def generator_text(count_symbol: str) -> str:
    """

    :param count_symbol:
    :return: random text
    """
    return " ".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(count_symbol))


def generator_csv(
        name_file: str = FILE_NAME,
        column: int = 0,
        line: int = 0,
        count_symbol: int = 0
) -> Union[bytes, str]:
    """
    Generator csv file write text in file
    :param name_file: file name
    :param column: column
    :param line:line
    :return: generate file csv
    """
    with open(name_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(line):
            writer.writerow([generator_text(count_symbol) for _ in range(column)])


def rewrite_text(text: str) -> str:
    """
    Iterator text
    :param text:
    :return:
    """
    for symbol in text:
        if symbol.isdigit() and int(symbol) % 2 > 0:
            yield "#"
        else:
            yield symbol


def reader(
        file_name: str = FILE_NAME,
        new_file_name: str = NEW_FILE_NAME
) -> Union[bytes, str]:
    """

    :param file_name: string file name
    :return: file
    """
    with open(file_name, newline='') as file:
        spam_reader = csv.reader(file, delimiter=',', quotechar='|')
        with open(new_file_name, 'w', newline='') as file_new:
            writer = csv.writer(file_new)
            for row in spam_reader:
                new_row = []
                for text in row:
                    if text[0] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                        new_row = []
                        break
                    else:
                        new_row.append("".join([symbol for symbol in rewrite_text(text)]))
                if new_row:
                    writer.writerow(new_row)


if __name__ == '__main__':
    print(f"""
    1 - task Сгенерировать csv файл из 1024 записей по 6 столбцов, заполненных строками случайных символов (цифры и латинские буквы) длиной по 8 символов. 
    B. Считать содержимое файла, заменить нечетные цифры символом #, удалить записи, в которых любая из шести строк начинается с гласной буквы, сохранить отредактированный файл с другим именем. 
    """
          )
    generator_csv(name_file=FILE_NAME, column=COLUMN, line=LINE, count_symbol=COUNT_SYMBOL)
    reader(file_name=FILE_NAME, new_file_name=NEW_FILE_NAME)