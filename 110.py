nl = [20, 34, 50, 48, 30, 100, 1050, 601, 460, 500, 205, 567, 650]
nl1 = filter((lambda x: True if x//50 == x/50 else False), nl)
print(list(nl1))
