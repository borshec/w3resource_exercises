import pathlib
p = "etc/init/test.ls"
pp = pathlib.Path(p)
sep = [pp.stem, pp.suffix[1:]]
print(sep)
