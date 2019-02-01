#!/usr/local/bin/python

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory

auth = PlainTextAuthProvider(username='dba', password='qxykVt!XTMVVjsn4$VWYJ6nLgd')
cluster = Cluster(['natl-vps-casdb01','natl-vps-casdb02','natl-vps-casdb03'], auth_provider = auth)
session = cluster.connect()

session.execute("insert into joe.accounts (id, source) values ('124', '{'name':'joe'};")
