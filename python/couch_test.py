#!/usr/local/bin/python

import couchdb

couch = couchdb.Server("http://172.16.248.227:5984/")
db = couch['joe']
rows = db.view('_all_docs', include_docs=True)

for row in rows:
    print(row)

