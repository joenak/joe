#!/usr/local/bin/python

import mysql.connector
import couchdb

conn = mysql.connector.connect(host='natl-vps-mema01'
    , user='vortex'
    , passwd='vortex'
    , db='vortex_topics')

cmd = 'select id, _source from vortex_topics.UARS limit 30;'

cursor = conn.cursor()
cursor.execute(cmd)
rows = cursor.fetchall()

couch = couchdb.Server("http://172.16.248.227:5984/")
db = couch['joe_test']

for row in rows:
    doc_id, doc_rev = db.save({row[0]: row[1]})


cursor.close()
conn.close()