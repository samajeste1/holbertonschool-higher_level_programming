#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa (SQL injection free!).
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

    # Execute SQL query with parameterized query (safe from SQL injection)
    # Only one execute() call
    cur.execute("""
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    # Fetch all rows
    query_rows = cur.fetchall()

    # Display results as comma-separated values
    city_names = [row[0] for row in query_rows]
    print(", ".join(city_names))

    # Close cursor and database connection
    cur.close()
    db.close()
