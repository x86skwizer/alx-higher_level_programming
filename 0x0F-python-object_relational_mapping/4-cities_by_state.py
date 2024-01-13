#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    curr = db.cursor()
    curr.execute("""SELECT cities.id, cities.name, states.name
                 FROM cities JOIN states ON cities.state_id=states.id
                 ORDER BY cities.id ASC""")
    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    db.close()
