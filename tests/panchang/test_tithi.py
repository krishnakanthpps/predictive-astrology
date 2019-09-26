import pytest

import sys
sys.path.append("/home/arunkhattri/github/predictive-astrology/src/")

from panchang.tithi import get_tithi
from pprint import pprint
pprint(sys.path)


def test_get_tithi():
    s_long = (5, 30, 37)
    m_long = (192, 37, 29)
    expected = ("pratipada", "krishna")
    actual = get_tithi(m_long, s_long)
    msg = f"Expected: {expected}; Actual: {actual}"
    assert actual == expected, msg
