import time
import random
import MySQLdb

db=MySQLdb.connect(user="root",db="dbmtest")

cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test (pkey INT NOT NULL PRIMARY KEY, value INT)")

pre_time = time.time()
# 1 Million loop
for x in range(1,1000000):
    cur.execute("INSERT INTO test VALUES (%d,%d)" % (x, x+x))
post_time = time.time()

print "Escribir 1M de registros: %.4f segundos" % (post_time-pre_time)

keys = [random.randint(1, 1000000) for x in range(1,10000)]
pre_time = time.time()
for x in keys:
    cur.execute("SELECT value FROM test WHERE pkey=%d" % x)
post_time = time.time()

print "Leer 10K registros aleatorios: %.4f segundos" % (post_time-pre_time)

pre_time = time.time()
cur.execute("SELECT value FROM test WHERE pkey>10000 and pkey<20000")
post_time = time.time()
print "Leer 10K registros consecutivos: %.4f segundos" % (post_time-pre_time)

db.close()
