import pathlib
import os
import time
p = pathlib.Path(".")
d = p.iterdir()
# for each in d:
#     if each.is_file():
#         print(each)
ls = {os.path.getctime(each): each.name for each in d if each.is_file()}
lss = sorted(ls.keys())
for each in lss:
    print("{}: {}".format(ls[each], time.asctime(time.gmtime(each))))
