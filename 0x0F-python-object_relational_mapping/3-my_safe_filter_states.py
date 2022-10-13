#!/usr/bin/python3
""" a script that is safe from MySQL injections"""
import MySQLdb
import sys

if __name__ = "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor

    cursor.execute("SELECT * FROM states WHERE name \
            LIKE %s ORDER BY id ASC", (sys.argv[4], ))
    query_rows = cursor.fetchall

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
