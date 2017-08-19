fd = int(input("Enter first digit:"))
sd = int(input("Enter second digit:"))
if fd == sd or fd+sd == 5 or abs(fd-sd) == 5:
    print("True")
else:
    print("False")
