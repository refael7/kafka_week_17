import os
import mysql.connector

mysql_conn = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'mysql'),
        user='user',
        password='password',
        database='app_db'
    )

cursor = mysql_conn.cursor()