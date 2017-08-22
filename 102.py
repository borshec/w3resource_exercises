import subprocess
s = subprocess.run(["ls", "-la"], stdout=subprocess.PIPE).stdout.decode()
print(s)
