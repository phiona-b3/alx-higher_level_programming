#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ = "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    # start cursor (cur=cursor, conn=connect)
    cur = conn.cursor()

    # query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    # print query
    for row in query_rows:
        print(row)

    # close cursor
    cur.close()
    conn.close()
