import pytest
from pyciters.ers2bib import gen_cite_key

def test_gen_cite_key():
    """
    Test the gen_cite_key function.
    """
    result = gen_cite_key(['Dylan Turner', 'Francis Tsiboe'], '2023-12-19')
    assert result == 'Turner_2023'

