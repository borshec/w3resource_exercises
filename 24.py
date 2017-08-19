vovels = ("e", "y", "u", "i", "a")
while True:
    lt = input("Enter letter:")
    if lt.isdecimal():
        break
    if lt in vovels:
        print("vovel")
    else:
        print("consonant")
