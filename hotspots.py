import os
import csv
import sqlite3

cloc = "cloc ./ --by-file --csv --quiet --report-file=cloc.csv"
cf = "git log --format=format: --name-only | egrep -v '^$' | sort | uniq -c | sort -r | sed -e 's/ *\([[:digit:]]*\) *\(.*\)/\\2,\\1/' > cf.csv"

if not os.path.exists("cloc.csv"):
    os.system(cloc)

if not os.path.exists("cf.csv"):
    os.system(cf)

conn = sqlite3.connect('hotspots.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS files")
c.execute('''
    CREATE TABLE files
    (name text, change_frequency int, blank int, comment int, code int)
''')

with open("cf.csv") as cf_file:
    cf_reader = csv.reader(cf_file, delimiter=",")
    for row in cf_reader:
        insert_sql = "INSERT INTO files VALUES ('{}', {}, null, null, null)".format(row[0], row[1])
        c.execute(insert_sql)

with open("cloc.csv") as cloc_file:
    cloc_reader = csv.reader(cloc_file, delimiter=",")
    for row in cloc_reader:
        update_sql = "UPDATE files SET blank={}, comment={}, code={} WHERE name='{}'".format(row[2], row[3], row[4], row[1])
        c.execute(update_sql)

conn.commit()
conn.close()

os.remove('cloc.csv')
os.remove('cf.csv')


