import pathlib
import os
import time
p = pathlib.Path("51.py")
print(time.asctime(time.gmtime(os.path.getctime(p))))
print(time.asctime(time.gmtime(os.path.getctime(p))))
print(time.asctime(time.gmtime(os.path.getatime(p))))
