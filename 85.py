import pathlib
p = pathlib.Path(".")
if p.is_file():
    print("file")
elif p.is_dir():
    print("directory")
