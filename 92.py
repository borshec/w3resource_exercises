ls = []
for each in range(255):
    ch = chr(each)
    if (not ch.isalnum()) and ch.isprintable():
        ls.append(ch)
print("".join(ls))
for each in ls:
    print("{0:>3s}, {1:>3x}, {1:0>8b}".format(each, ord(each)))
