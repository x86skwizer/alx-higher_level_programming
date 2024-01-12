#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))
    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    db.close()
