import os
id = []
id.append(os.getuid())
id.append(os.getgid())
id.append(os.geteuid())
id.append(os.getegid())
id.append(os.getgroups())
print(id)
