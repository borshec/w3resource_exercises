import re
n = re.findall(r"\d+", input("Enter 3 separated numbers:"))
n = [int(i) for i in n[:3]]
print(sum(n))
