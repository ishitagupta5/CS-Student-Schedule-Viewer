import sqlite3
import sys
from os.path import exists

# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 2:
    print("Usage: python script_name.py academic_year")
    sys.exit(1)

academic_year = int(sys.argv[1])

if exists('cs_course_scheduling.sqlite'):
    conn = sqlite3.connect('cs_course_scheduling.sqlite')

    # Construct SQL query dynamically with the provided academic year
    query = "SELECT first_name, last_name, academic_year FROM students WHERE academic_year = {} ORDER BY last_name".format(academic_year)

    cursor = conn.execute(query)
    for row in cursor:
        print("First Name = ", row[0])
        print("Last Name = ", row[1])
        print("Academic Year = ", row[2])
        print("----------------------------------------")

    conn.close()
    print("Database was accessed and closed")
else:
    print('Database file cs_course_scheduling.sqlite not found in the current working directory.')
