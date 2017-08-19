import sys
for each in sys.path:
    if each.find("site-packages") > 0:
        print(each)
