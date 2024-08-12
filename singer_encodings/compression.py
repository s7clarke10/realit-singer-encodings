"""A helper function to detected supported compressed files."""

from __future__ import annotations

import gzip
import zipfile


def infer(iterable, file_name):
    """Uses the incoming file_name and checks the end of the string
    for supported compression types"""
    if not file_name:
        raise ValueError("Need file name")

    if file_name.endswith(".tar.gz"):
        raise NotImplementedError("tar.gz not supported")
    if file_name.endswith(".gz"):
        yield gzip.GzipFile(fileobj=iterable)
    elif file_name.endswith(".zip"):
        with zipfile.ZipFile(iterable) as unzip_file:
            # pylint: disable=consider-using-with
            for name in unzip_file.namelist():
                yield unzip_file.open(name)
    else:
        yield iterable
