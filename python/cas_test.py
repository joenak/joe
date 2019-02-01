#!/usr/local/bin/python

from cassandra.query import dict_factory
from cassandra.cluster import Cluster

cluster = Cluster(['172.16.248.228'])

session = cluster.connect('joe')
session.row_factory = dict_factory
rows = session.execute("SELECT id, source FROM joe.uars LIMIT 10")

for row in rows:
    print(row)
