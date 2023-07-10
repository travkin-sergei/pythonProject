import psycopg2
from psycopg2 import Error
from config import db_password
# ddddd

def sql_query(user_id, user_first_name, user_last_name, user_username, word):
    try:
        connection = psycopg2.connect(
            user=db_password['user'],
            password=db_password['password'],
            host=db_password['host'],
            port=db_password['port'],
            database=db_password['database']
        )

        cursor = connection.cursor()
        sql = """ INSERT INTO user_word
        (user_id, user_first_name, user_last_name, user_username, word)
        VALUES( %s, %s, %s, %s, %s, %s)"""

        cursor.execute(sql, (user_id, user_first_name, user_last_name, user_username, word))
        connection.commit()

    except (Exception, Error) as error:
        if error == 'not all arguments converted during string formatting':
            error = 'не все аргументы преобразуются при форматировании строки'

    finally:
        if connection:
            cursor.close()
            connection.close()


def sql_quey(word):
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(
            user=db_password['user'],
            password=db_password['password'],
            host=db_password['host'],
            port=db_password['port'],
            database=db_password['database']
        )

        cursor = connection.cursor()

        sql = """SELECT description FROM word_set WHERE word = %s"""

        cursor.execute(sql, (word,))
        data = cursor.fetchone()
        data = data[0]
        sss = ''
        for i in data:
            sss = sss + ' ' + data[i] + '\n'


    except (Exception, Error) as error:
        if error == 'not all arguments converted during string formatting':
            error = 'не все аргументы преобразуются при форматировании строки'

    finally:
        if connection:
            cursor.close()
            connection.close()
    return data


def sql_quey_complaint_set():
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(
            user=db_password['user'],
            password=db_password['password'],
            host=db_password['host'],
            port=db_password['port'],
            database=db_password['database']
        )

        cursor = connection.cursor()

        sql = """SELECT ((date_from::date)::text ||'\n'|| name||'\n'|| description) as data FROM complaint_set"""

        cursor.execute(sql)
        data = cursor.fetchall()


    except (Exception, Error) as error:
        if error == 'not all arguments converted during string formatting':
            error = 'не все аргументы преобразуются при форматировании строки'

    finally:
        if connection:
            cursor.close()
            connection.close()
    return data

