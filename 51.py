import os
f = input("Enter script name:")
os.system("python -m cProfile {0}".format(f))
