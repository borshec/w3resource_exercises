import re
s = input("Enter string:")
if not re.match("[Ii]s\s", s):
    s = "Is " + s
print(s)
