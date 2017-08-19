s = " d ddjdjdj jdjdje xjfnd \n djdjsj djdje \n ndjdje"
print(s)
s = s.replace(" ", "")
s = s.replace("\n", "")
print(s)
for each in s:
    print(each, sep="", end="")
