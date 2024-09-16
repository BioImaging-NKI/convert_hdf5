"""
Copy data in an imaris file that has been compressed with LZ4 to gzip.
"""

from hdf5converter import copydata
from pathlib import Path

pth_in = Path(r"c:\test.ims")
pth_out = Path(pth_in.parent, pth_in.stem + "_converted.ims")
if not pth_out.exists():
    copydata(pth_in, pth_out, compression="gzip")
