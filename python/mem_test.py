#!/usr/local/bin/python

import mysql.connector


conn = mysql.connector.connect(host='172.16.248.226'
    , user='root'
    , passwd='joe'
    , db='joe')

cmd = 'select id, _source from joe.UARS limit 10;'

cursor = conn.cursor()
cursor.execute(cmd)
rows = cursor.fetchall()

for row in rows:
    print(row[0], row[1])

cursor.close()
conn.close()