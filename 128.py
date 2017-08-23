import re
s = "DNDJDtDDJDJD"
res = re.search("[a-z]", s)
if res is not None:
    print("Exist")
