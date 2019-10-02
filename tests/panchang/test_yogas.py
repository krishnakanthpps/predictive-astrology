import pytest
import sys
sys.path.append("/home/arunkhattri/github/predictive-astrology/src/")

from panchang.yogas import get_yogas


class TestGetTithi():

    def test_vishkumbha(self):
        m_long = (192, 37, 29)
        s_long = (5, 30, 37)
        actual = get_yogas(m_long, s_long)
        expected = "vishkumbha"
        msg = "actual: {actual}; expected: {expected}"
        assert actual == expected, msg
