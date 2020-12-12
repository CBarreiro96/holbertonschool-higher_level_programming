#!/usr/bin/python3
# List all states with a name starting with uppercase N
# Username, password, and database names are given as user args
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT states.id, name FROM states WHERE name "
                "COLLATE latin1_general_cs "
                "LIKE 'N%' "
                "ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
