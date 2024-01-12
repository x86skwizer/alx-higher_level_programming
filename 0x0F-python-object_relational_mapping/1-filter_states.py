#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    curr = db.cursor()
    curr.execute("SELECT * FROM states")
    rows = curr.fetchall()
    for row in rows:
        if (row[1][0] == 'N'):
            print(row)
    curr.close()
    db.close()
