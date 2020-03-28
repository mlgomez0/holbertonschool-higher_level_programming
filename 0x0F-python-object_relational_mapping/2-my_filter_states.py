#!/usr/bin/python3
"""script to print name starting with N form a table using MySQLdb"""
import MySQLdb
import sys
if __name__ == "__main__":
    state_in ="'" + sys.argv[4] + "'"
    print(state_in)
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT DISTINCT id,\
                name FROM states WHERE name = @state_in ORDER BY id ASC")

    rows = cur.fetchall()
    for r in rows:
        print(r)
