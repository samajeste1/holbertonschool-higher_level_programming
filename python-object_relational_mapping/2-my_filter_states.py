#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create cursor object
    cur = db.cursor()

    # Execute SQL query using format (vulnerable to SQL injection)
    query = "SELECT * FROM states WHERE BINARY name = '{}' \
ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Fetch all rows
    query_rows = cur.fetchall()

    # Display results
    for row in query_rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
