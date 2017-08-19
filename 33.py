fd = int(input("Enter first digit:"))
sd = int(input("Enter second digit:"))
td = int(input("Enter third digit:"))
if fd == sd or sd == td or fd == td:
    res = 0
else:
    res = fd+sd+td
print(res)
