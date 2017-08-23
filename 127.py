i = 3848248448484484888737
s = i.bit_length()
if s > 64:
    print("no fits, ({})".format(s))
else:
    print("fits, ({})".format(s))
