#!/usr/bin/python3
import MySQLdb
import sys
db = MySQLdb.connect(user=sys.argv[1],passwd=sys.argv[2],db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT id, name FROM states")
rows = cur.fetchall()
for r in rows:
    print(r)
