2.1.1 (2024-08-19)
**Changes**
  - Moving to a trusted push to pypi

2.1.0  (2024-08-12)
-------------------
**Changes**
  - Making a variant realit-singer-encodings
  - Moving from setup.py to project.toml and Poetry instead of setup tools
  - Adding ci/cd pipelines for running pytest
  - Adding publishing pipeline to pypi
  - Adding tox to run ci tests before raising a PR
  - Linting code
  - Adding README.md

2.0.13 (2023-10-07)
-------------------
**Changes**
  - Configurable characterset format. Option='encoding'
  - Ability to remove a character. Option='remove_character'
  - Removed dependency on singer-python
  - Ensured that utf-8-sig (default encoding) is used to detect the signature for the likes of BOM metadata.
  - Added dependabot monitoring
