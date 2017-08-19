import sys
import pathlib
import shutil
psrc = pathlib.Path(sys.argv[0])
# pdest = pathlib.Path(sys.argv[0]+"_")
pdest2 = psrc.with_suffix(".copy")
shutil.copyfile(psrc, pdest2)
