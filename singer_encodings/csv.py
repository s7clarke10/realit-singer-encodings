from __future__ import annotations

import codecs
import csv

from singer_encodings.csv_helper import SDC_EXTRA_COLUMN, CSVHelper

from . import compression


def get_row_iterators(iterable, options=None, infer_compression=False):
    """Accepts an interable, options and a flag to infer compression and yields
    csv.DictReader objects which can be used to yield CSV rows."""
    if options is None:
        options = {}
    if infer_compression:
        compressed_iterables = compression.infer(
            iterable, options.get("file_name")
        )

    # pylint: disable=possibly-used-before-assignment
    for item in compressed_iterables:
        yield get_row_iterator(item, options=options)


def get_row_iterator(
    iterable,
    options=None,
    headers_in_catalog=None,
    with_duplicate_headers=False,
):
    """Accepts an interable, options and returns a csv.DictReader or csv.Reader object
    which can be used to yield CSV rows.
    When with_duplicate_headers == true, it will return csv.Reader object
    When with_duplicate_headers == false, it will return csv.DictReader object (default)
    """

    options = options or {}
    reader = []
    headers = set()
    file_stream = codecs.iterdecode(
        iterable, encoding=options.get("encoding", "utf-8-sig")
    )
    delimiter = options.get("delimiter", ",")
    remove_character = options.get("remove_character", "")

    # Return the CSV key-values along with considering the duplicate headers,
    # if any, in the CSV file
    if with_duplicate_headers:
        # CSV Helper is used to handle duplicate headers.
        # It will store the duplicate headers and its value in the '_sdc_extra' field
        csv_helper = CSVHelper()
        reader = csv_helper.get_row_iterator(
            file_stream, delimiter, headers_in_catalog
        )
        headers = set(csv_helper.unique_headers)
    else:
        if remove_character:
            # Replace any NULL bytes and 'remove_character' in the line
            # given to the DictReader
            reader = csv.DictReader(
                (
                    line.replace("\0", "").replace(remove_character, "")
                    for line in file_stream
                ),
                fieldnames=None,
                restkey=SDC_EXTRA_COLUMN,
                delimiter=delimiter,
            )
        else:
            # Replace any NULL bytes in the line given to the DictReader
            reader = csv.DictReader(
                (line.replace("\0", "") for line in file_stream),
                fieldnames=None,
                restkey=SDC_EXTRA_COLUMN,
                delimiter=delimiter,
            )
        try:
            headers = set(reader.fieldnames)
        except TypeError:
            # handle Nonetype error when empty file is found: tap-SFTP
            pass

    if options.get("key_properties"):
        key_properties = set(options["key_properties"])
        if not key_properties.issubset(headers):
            raise ValueError(
                f"CSV file missing required headers: {key_properties - headers}"
            )

    if options.get("date_overrides"):
        date_overrides = set(options["date_overrides"])
        if not date_overrides.issubset(headers):
            raise ValueError(
                f"CSV file missing date_overrides headers: {date_overrides - headers}"
            )
    return reader
