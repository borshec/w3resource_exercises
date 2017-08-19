import timeit
import re
import time


def test():
    s = " jfndjsj sbdheje dheheje dehejej"
    return re.findall(r'\w', s)


# t = timeit.timeit(stmt="test()", setup="from __main__ import test", number=1000)
# print(t)

t = time.time()
n = 1000
for each in range(n):
    test()
print(time.time()-t)
