import re
sd = input("Sample data:")
ls = re.findall(r"\d+", sd)
tp = tuple(ls)
print("List:", ls)
print("Tuple:", tp)
