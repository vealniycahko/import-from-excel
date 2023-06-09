import psycopg2

SPREADSHEET_PATH = ''

def get_pg_connection():
    conn = psycopg2.connect(host='',
                            port='',
                            database='',
                            user='',
                            password='')
    conn.autocommit = True
    return conn
