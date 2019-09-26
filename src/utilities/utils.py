"""Utiliy functions for calculation of panchang"""

import math


def dms_to_dd(degrees):
    """
    :param degrees: tuple(degree, minute, secoonds)
    :return:decimal degrees
    """
    deg, min, sec = degrees
    dd = deg + (min/60) + (sec / (60 * 60))
    return dd


def dd_dms(dd):
    """
    :params dd: degrees in decimal notation
    :return: degree, minutes, seconds
    """
    is_positive = dd >= 0
    dd = abs(dd)
    minutes, seconds = divmod(dd * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    if not is_positive:
        degrees = -degrees
    return (degrees, minutes, seconds)


def diff_long(moon_long, sun_long):
    """
    :param moon_long: tuple(degree, minute, secoonds)
    :param sun_long: tuple(degree, minute, secoonds)
    :return:difference of longitudes of moon and sun in radians, float
    """
    m_rad = math.radians(dms_to_dd(moon_long))
    # print(m_rad)
    s_rad = math.radians(dms_to_dd(sun_long))
    # print(s_rad)
    if m_rad > s_rad:
        diff = m_rad - s_rad
    else:
        m_rad += math.radians(360)
        diff = m_rad - s_rad
    return diff
