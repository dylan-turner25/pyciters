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
The `pyciters` has a single primary function, `cite_ers`, which takes a url or list of urls corresponding to [USDA ERS publications](https://www.ers.usda.gov/publications) and returns bibtex citation entries than can be copied as plain text into a .bib file or used in any citation manager that can import bibtex entries (ex: Zotero). 

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
The above output can be copied and if using [Zotero]("https://www.zotero.org/"), selecting `File->Import from Clipboard` will import the citation into your library. 

## Examples
Multiple urls can be passed to the `citer_ers` function if there are multiple publications to generate citatios for.
```python
# list of urls to generate citations for
pubs_to_cite = ["https://www.ers.usda.gov/publications/pub-details?pubid=110093",
                "https://www.ers.usda.gov/publications/pub-details?pubid=108166"]

# pass the list to the cite_ers function
cite_ers(pubs_to_cite)

```
The output is multiple bibtext entries as plain text than can be copied into a .bib file.

```console
@misc{Baldwin_2024,
author = {Katherine L. Baldwin AND Dylan Turner AND Francis Tsiboe},
title = {Recent Developments in Ad Hoc Assistance Programs for Agricultural Producers},
publisher = {U.S. Department of Agriculture, Economic Research Service},
howpublished = {Economic Information Bulletin},
year = {2024},
month = {9},
number = {EIB-278},
url = {https://www.ers.usda.gov/publications/pub-details?pubid=110093}
}

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

The publication IDs associated with the ERS publication can also be used to generate the citation.

```python
# list of publication IDs to generate citations for
pubs_to_cite = [110093,108166]

# pass the list to the cite_ers function
cite_ers(pubs_to_cite)

```

## License

`pyciters` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
