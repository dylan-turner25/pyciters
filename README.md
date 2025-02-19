# pyciters

[![PyPI - Version](https://img.shields.io/pypi/v/citers.svg)](https://pypi.org/project/citers)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/citers.svg)](https://pypi.org/project/citers)
[![Python package](https://github.com/dylan-turner25/pyciters/actions/workflows/python-package.yml/badge.svg)](https://github.com/dylan-turner25/pyciters/actions/workflows/python-package.yml)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install citers
```

## Usage
```python
# import the citer_ers function
from pyciters.ers2bib import cite_ers

# call the function with a url to a publication to cite
cite_ers("https://www.ers.usda.gov/publications/pub-details?pubid=108166")
```

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

## License

`citers` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
