import sqlite3
from os.path import exists
import sys

if len(sys.argv) != 2:
    print("Usage: python script_name.py academic_year")
    sys.exit(1)

academic_year = int(sys.argv[1])

if exists('cs_course_scheduling.sqlite'):
    conn = sqlite3.connect('cs_course_scheduling.sqlite')
    query = "SELECT first_name, last_name, academic_year FROM students WHERE academic_year = {} ORDER BY last_name".format(academic_year)
    cursor = conn.execute(query)
    
    html_content = "<html><head><title>Students in Academic Year {}</title></head><body>".format(academic_year)
    html_content += "<h1>Students in Academic Year {}</h1>".format(academic_year)
    html_content += "<table border='1'><tr><th>First Name</th><th>Last Name</th><th>Academic Year</th></tr>"
    
    for row in cursor:
        html_content += "<tr>"
        html_content += "<td>{}</td>".format(row[0])
        html_content += "<td>{}</td>".format(row[1])
        html_content += "<td>{}</td>".format(row[2])
        html_content += "</tr>"
    
    html_content += "</table></body></html>"

    conn.close()
    
    with open("students_academic_year_{}.html".format(academic_year), "w") as html_file:
        html_file.write(html_content)

    print("HTML file created successfully.")
else:
    print('Database file cs_course_scheduling.sqlite not found in the current working directory.')