import os
import pathlib
import re
pt = "[45][1-7]\w*.py$"
p = pathlib.Path(os.getcwd())
for f in p.iterdir():
    f = f.name
    if re.search(pt, f) is not None:
        print(f)
