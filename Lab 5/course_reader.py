__author__ = 'kq4hy'

import csv
import sqlite3


def load_course_database(db_name, csv_filename):
    conn = sqlite3.connect(db_name)
    with conn:
        curs = conn.cursor()
        with open(csv_filename, 'rU') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                sql_cmd = "insert into coursedata values(?, ?, ?, ?, ?, ?, ?)"
                curs.execute(sql_cmd, row)

load_course_database('course1.db', 'seas-courses-5years.csv')