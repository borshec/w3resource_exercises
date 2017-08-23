ls = [3, -5, 8, 0, 2, -3, -1, -0, 7]
nl = list(filter((lambda x: True if x > 0 else False), ls))
print(nl)
