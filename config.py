import psycopg2

SPREADSHEET_PATH = '/home/vealniycahko/STUDY/Code/excel_parsing/testing.xlsx'

def get_pg_connection():
    conn = psycopg2.connect(host='127.0.0.1',
                            port='5454',
                            database='postgres',
                            user='postgres',
                            password='postgres')
    conn.autocommit = True
    return conn
