#!/usr/local/bin/python

import mysql.connector
from cassandra.query import dict_factory
from cassandra.cluster import Cluster

conn = mysql.connector.connect(host='natl-vps-mema01'
    , user='vortex'
    , passwd='vortex'
    , db='vortex_topics')

cmd = 'select id, _source from vortex_topics.UARS limit 30;'

cursor = conn.cursor()
cursor.execute(cmd)
rows = cursor.fetchall()

cluster = Cluster(['natl-vps-casdb01','natl-vps-casdb02','natl-vps-casdb03'])
session = cluster.connect('joe')
session.row_factory = dict_factory

for row in rows:
    session.execute("insert into joe.uars (id, source) values (%s, %s);", (row[0], row[1]))

cursor.close()
conn.close()