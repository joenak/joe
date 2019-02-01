#!/usr/local/bin/python

import mysql.connector

conn = mysql.connector.connect(host='natl-vps-mema01'
    , user='vortex'
    , passwd='vortex'
    , db='vortex_topics')

conn2 = mysql.connector.connect(host='172.16.248.226'
    , user='root'
    , passwd='joe'
    , db='joe')

cmd = 'select id, _source from vortex_topics.UARS limit 100000;'

cursor = conn.cursor()
cursor.execute(cmd)
rows = cursor.fetchall()

cursor2 = conn2.cursor()

for row in rows:
    cursor2.execute("insert into joe.UARS (id, _source) values (%s, %s);", (row[0], row[1])) 
    print(row[0])

conn2.commit()

cursor2.close()
conn2.close()
cursor.close()
conn.close()