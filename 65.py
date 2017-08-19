import time
import datetime
s = int(input("Enter seconds:"))
t0 = time.time()
t1 = t0 + s
d0 = datetime.datetime.fromtimestamp(t0)
d1 = datetime.datetime.fromtimestamp(t1)
print(d1-d0)
