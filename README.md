# pyciters

[![PyPI - Version](https://img.shields.io/pypi/v/citers.svg)](https://pypi.org/project/citers)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/citers.svg)](https://pypi.org/project/citers)
[![Python package](https://github.com/dylan-turner25/pyciters/actions/workflows/python-package.yml/badge.svg)](https://github.com/dylan-turner25/pyciters/actions/workflows/python-package.yml)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation
The `pyciters` package can be installed directly from github.
```console
pip install git+https://github.com/dylan-turner25/pyciters
```

## Usage
The `pyciters` has a single primary function, `cite_ers`, which takes a url or list of urls corresponding to USDA ERS publications and returns bibtex citation entries than can be copied as plain text and used in any citation manager than import bibtex entries (ex: Zotero). 

```python
# import the citer_ers function
from pyciters.ers2bib import cite_ers

# call the function with a url to a publication to cite
cite_ers("https://www.ers.usda.gov/publications/pub-details?pubid=108166")
```
Example output:
```console
@misc{Turner_2023,
author = {Dylan Turner AND Francis Tsiboe AND Katherine L. Baldwin AND Brian Williams AND Erik Dohlman AND Gregory Astill AND Sharon Raszap Skorbiansky AND Vidalina Abadam AND D. Adeline Yeh AND Russell Knight},
title = {Federal Programs for Agricultural Risk Management},
publisher = {U.S. Department of Agriculture, Economic Research Service},
howpublished = {Economic Information Bulletin},
year = {2023},
month = {12},
number = {EIB-259},
url = {https://www.ers.usda.gov/publications/pub-details?pubid=108166}
}
```
The above output can be copied and if using Zotero, selecting `File->Import from Clipboard` will import the citation into your library. 

## Other examples
Multiple urls can be passed to the `citer_ers` function if there are multiple publications to generate citatios for.
```python
# list of urls to generate citations for
pubs_to_cite = []

# pass the list to the cite_ers function
cite_ers(pubs_to_cite)

```

```console


```

The publication IDs associated with the ERS publication can also be used to generate the citation.
```python
# list of publication IDs to generate citations for
pubs_to_cite = []

# pass the list to the cite_ers function
cite_ers(pubs_to_cite)

```

```console

```


## License

`pyciters` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
