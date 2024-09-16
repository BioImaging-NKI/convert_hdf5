# Convert HDF5 to HDF5
The [Imaris File Format](https://imaris.oxinst.com/support/imaris-file-format) is actually [HDF5](https://www.hdfgroup.org/) underneath. It has support for LZ4 compressed datasets, however this is not supported by bioformats. This code convert HDF5 to HDF5 but converts all previously compressed datasets to gzip compression. Hopefully it will become obsolete soon.

## Install
* Clone the repository
* `pip install -e .`

## Usage
```
from hdf5converter import copydata
from pathlib import Path

pth_in = Path(r"c:\file_in.ims")
pth_out = Path(r"c:\file_out.ims")
copydata(pth_in, pth_out, compression="gzip")
```