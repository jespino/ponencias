from kyotocabinet import *
import time
import random

db = DB()
db.open("db.kch", DB.OCREATE|DB.OWRITER)

pre_time = time.time()
# 1 Million loop
for x in range(1,1000000):
    db.add(x,x+x)
post_time = time.time()

print "Escribir 1M de registros: %.4f segundos" % (post_time-pre_time)

keys = [random.randint(1, 1000000) for x in range(1,10000)]
pre_time = time.time()
for x in keys:
    db.get(x)
post_time = time.time()

print "Leer 10K registros aleatorios: %.4f segundos" % (post_time-pre_time)

cur = db.cursor()
pre_time = time.time()
cur.jump(10000)
for x in range(1,10000):
    cur.step()
post_time = time.time()
print "Leer 10K registros consecutivos: %.4f segundos" % (post_time-pre_time)

db.close()
