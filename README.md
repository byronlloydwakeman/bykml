## Introduction

**bykml** is a library for reading, writing, and updating KML files.
It uses dictionaries to make replacing values and adding KML elements simple.

## Documentation

The `kmlfactory` module inside the `bykml` package provides:

- `KmlFactory` class
- `placemark_template` function

These are used to create placemarks and add them to a KML structure.

## Install

```bash
pip install bykml
```

## Dependencies

- [xmltodict](https://pypi.org/project/xmltodict/)

## Limitations

Because Python dictionaries can only hold one value per key, lists must be used when a KML tag needs multiple child items.

For example, a `Folder` containing multiple placemarks must represent those placemarks as a list.
Support for more flexible nested structures is currently under review.

For release history, see [CHANGELOG.md](./CHANGELOG.md).
