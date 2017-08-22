import pathlib
fsi = input("Enter name")
p = pathlib.Path(fsi)
if p.is_file():
    print("File")
elif p.is_dir():
    print("Directory")
