import pytest

import sys
sys.path.append("/home/arunkhattri/github/predictive-astrology/src/")

from panchang.tithi import get_tithi
# from pprint import pprint
# pprint(sys.path)


class TestGetTithi():

    def test_str_in_input(self):
        s_long = ('five', 30, 37)
        m_long = (192, 37, 29)
        expected = None
        actual = get_tithi(m_long, s_long)
        msg = f"Expected: {expected}; Actual: {actual}"
        assert actual == expected, msg

    def test_len_less_than_three(self):
        s_long = (30, 37)
        m_long = (192, 37, 29)
        expected = None
        actual = get_tithi(m_long, s_long)
        msg = f"Expected: {expected}; Actual: {actual}"
        assert actual == expected, msg

    def test_pratipada_tithi(self):
        s_long = (5, 30, 37)
        m_long = (192, 37, 29)
        expected = ("pratipada", "krishna")
        actual = get_tithi(m_long, s_long)
        msg = f"Expected: {expected}; Actual: {actual}"
        assert actual == expected, msg
    
    def test_amavasya_tithi(self):
        s_long = (272, 42, 18)
        m_long = (271, 40, 14)
        expected = ("amavasya", "krishna")
        actual = get_tithi(m_long, s_long)
        msg = f"Expected: {expected}; Actual: {actual}"
        assert actual == expected, msg

    def test_purnima_tithi(self):
        s_long = (286, 56, 33)
        m_long = (99, 6, 13)
        expected = ("purnima", "shukla")
        actual = get_tithi(m_long, s_long)
        msg = f"Expected: {expected}; Actual: {actual}"
        assert actual == expected, msg
