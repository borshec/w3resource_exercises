ls = ["qw", "er", "ty", 1, "as", 2, "df", 3, "gh"]
ls = [str(i) for i in ls]
st = "".join(ls)
ba = bytearray(st, "utf-8")
ba[0] = ord("x")
print(ba)
