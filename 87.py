import os
import pathlib
f = pathlib.Path("50.py")
s = f.stat()
ss = s.st_size
print(ss)
