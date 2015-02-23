__author__ = 'kq4hy'

import csv
import sqlite3


def load_course_database(db_name, csv_filename):
    conn = sqlite3.connect(db_name)
    with open(csv_filename, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            with conn:
                cur = conn.cursor()
                sql_cmd = "insert into coursedata values(row[0], row[1], row[2], row[3], row[4], row[5], row[6])"
                cur.execute(sql_cmd)

load_course_database('course1.db', 'seas-courses-5years.csv')