import math
fd = int(input("Enter first digit:"))
sd = int(input("Enter second digit:"))
print(abs(fd*sd)//math.gcd(fd, sd))
