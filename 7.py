import re
fn = input("Sample filename:")
ext = re.search(r"\.(\w+)", fn).group(1)
print(ext)
