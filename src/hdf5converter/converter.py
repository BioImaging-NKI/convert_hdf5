import os
from typing import Union, Any
import h5py
import hdf5plugin


def copydata(
    pth_in: Union[str, os.PathLike[Any]],
    pth_out: Union[str, os.PathLike[Any]],
    compression: str = "gzip",
) -> None:
    with h5py.File(pth_out, "w") as f_dst:
        with h5py.File(pth_in, "r") as f_src:
            for a in f_src.attrs.keys():
                f_dst.attrs.create(a, f_src.attrs[a])
            for k in f_src.keys():
                recursivecopy(f_src, f_dst, k, compression=compression)


def recursivecopy(
    f_src: h5py.File, f_dst: h5py.File, name: str, compression: str
) -> None:
    if isinstance(f_src[name], h5py.Group):
        print(f"I copy Group {name}")
        f_dst.create_group(name)
        for a in f_src[name].attrs.keys():
            f_dst[name].attrs.create(a, f_src[name].attrs[a])
        for k in f_src[name].keys():
            recursivecopy(f_src, f_dst, name + "/" + k, compression=compression)
    elif isinstance(f_src[name], h5py.Dataset):
        print(f"I copy DataSet {name}")
        plist = f_src[name].id.get_create_plist()
        for i in range(plist.get_nfilters()):
            print(f"Found filter: {plist.get_filter(i)}")
        if plist.get_nfilters() > 0:  # has compression
            f_dst.create_dataset(
                name,
                data=f_src[name][:],
                compression=compression,
                chunks=f_src[name].chunks,
            )
        else:
            f_dst.create_dataset(name, data=f_src[name][:])
        for a in f_src[name].attrs.keys():
            f_dst[name].attrs.create(a, f_src[name].attrs[a])
    else:
        print(f"ERROR: {name} is of type {type(f_src[name])}")
