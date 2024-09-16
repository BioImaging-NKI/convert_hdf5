import pytest as pytest
from pathlib import Path
from hdf5converter import copydata


@pytest.fixture
def file():
    return Path(Path.cwd(), "tests", "testdata", "PyImarisWriterTest.ims")


def test_conversion(file):
    assert file.exists()
    out = Path(file.parent, file.stem + "_convert.ims")
    copydata(file, out, compression='gzip')
    assert out.exists()
    stat = out.stat()
    assert stat.st_size == 1830136
    out.unlink()

