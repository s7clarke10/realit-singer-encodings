realit-singer-encodings
===================
[![PyPI version](https://badge.fury.io/py/realit-singer-encodings.svg)](https://badge.fury.io/py/realit-singer-encodings)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/realit-singer-encodings.svg)](https://pypi.org/project/realit-singer-encodings/)
[![License: MIT](https://img.shields.io/badge/License-Apache2-yellow.svg)](https://opensource.org/licenses/Apache-2.0)

Writes the Singer format from Python.

This is a fork of [Singer's singer-encodings](https://github.com/singer-io/singer-encodings) made for [PipelineWise](https://transferwise.github.io/pipelinewise) and [Meltano](https://meltano.com/).

Usage
---

### Setup environment
This library depends on python3. We recommend using a `virtualenv` like this:

```bash
python3 -m venv ~/.virtualenvs/realit-singer-encodings
```

### Installation
Next, install this library:

```bash
source ~/.virtualenvs/realit-singer-encodings/bin/activate
git clone http://github.com/s7clarke10/realit-singer-encodings
cd realit-singer-encodings
pip install .
```

### Usage example

This package is used by tap-s3-csv. One of the key configurable items is the `table` field.
The `table` field consists of one or more objects, that describe how to find files and emit records. A more detailed (and unescaped) example below:

```
[
    {
        "search_prefix": "exports"
        "search_pattern": "my_table\\/.*\\.csv",
        "table_name": "my_table",
        "key_properties": ["id"],
        "date_overrides": ["created_at"],
        "delimiter": ",",
        "guess_types": true,
        "string_overrides": ["field_1","field_2"],
        "remove_character": "\""
    },
    ...
]
```

The following specific settings influence the behaviour of the singer-encodings package.

- **string_overrides**: Specifies field names in the files that should be parsed as a string regardless of what was discovered.
- **guess_types**: (default `true`) By default, column data types will be determined via scanning the first file in a table_spec. Set this to `false` to disable this and set all columns to `string`.
- **remove_character**: Specifies a character which can be removed from each line in the the file e.g. `"\""` will remove all double-quotes.
- **encoding**: The encoding to use to read these files from [codecs -> Standard Encodings](https://docs.python.org/3/library/codecs.html#standard-encodings)

## Developer Resources

### Initialize your Development Environment

```bash
pip install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests/` directory and
then run:

```bash
poetry run pytest
```

or 

```bash
poetry run coverage run --parallel -m pytest
```

### Continuous Integration
Run through the full suite of tests and linters by running

```bash
poetry run tox
```

These must pass in order for PR's to be merged.

License
-------

Distributed under the Apache License Version 2.0
