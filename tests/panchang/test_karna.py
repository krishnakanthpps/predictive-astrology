"""Tests for src/panchang/karna.py"""
import pytest
import sys
sys.path.append("/home/arunkhattri/github/predictive-astrology/src/")

from panchang.karna import get_karna


class TestGetKarna():
    """Tests for get_karna"""

    def test_kaulava(self):
        m_long = (192, 37, 29)
        s_long = (5, 30, 37)
        actual = get_karna(m_long, s_long)
        expected = "kaulava"
        msg = f"actual: {actual}; expected: {expected}"
        assert actual == expected, msg
