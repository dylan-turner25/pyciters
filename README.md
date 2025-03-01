# pyciters

<!--
[![PyPI - Version](https://img.shields.io/pypi/v/citers.svg)](https://pypi.org/project/citers)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/citers.svg)](https://pypi.org/project/citers)
-->

[![Python package](https://github.com/dylan-turner25/pyciters/actions/workflows/python-package.yml/badge.svg)](https://github.com/dylan-turner25/pyciters/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/dylan-turner25/pyciters/graph/badge.svg?token=Z65ezjE7oe)](https://codecov.io/gh/dylan-turner25/pyciters)
-----

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Overview
The [USDA Economic Research Service](https://www.ers.usda.gov/) (ERS) publishes a huge amount of research relevant to the agricultural sector. These research reports are often relevant to other academic research. The `pyciters` package is a simple utility that generates bibtex citation entries using the url of a ERS report in an attempt to make life slightly easier for anyone that cites these reports on a regular basis. 


## Installation
The `pyciters` package can be installed directly from github.
```console
pip install git+https://github.com/dylan-turner25/pyciters
```

## Usage
The `pyciters` has a single module `ers2bib` and single class, `Publication`, which takes the url or list of urls corresponding to [USDA ERS publications](https://www.ers.usda.gov/publications) as an single argument. The resulting publication object has an attribute `meta_data` that contains each publication's meta data fields in a data frame.

```python
from pyciters import ers2bib

# create a publication object
pubs = ers2bib.Publication(["https://www.ers.usda.gov/publications/pub-details?pubid=110093",
                "https://www.ers.usda.gov/publications/pub-details?pubid=108166"])


# pull up the publication meta data
pubs.meta_data

```

Using the `generate_citation` method will return bibtex citation entries that can be copied as plain text into a .bib file or used in any citation manager that can import bibtex entries (ex: Zotero). 

```python
pubs.generate_citation()
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
The above output can be copied, and if using [Zotero]("https://www.zotero.org/"), selecting `File->Import from Clipboard` will import the citation into your library. 

## Examples

The publication IDs associated with the ERS publication can also be used to generate the citation.

```python
# create publication object using report id numbers
pubs = ers2bib.Publication([110093,108166])

# create the bibtex entries
pubs.generate_citation()

```

## License

`pyciters` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
