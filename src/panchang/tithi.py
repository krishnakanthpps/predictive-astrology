"""Calculate tithi for a given day"""

import math
from utilities import utils

TITHI_NAME = ['pratipada', 'dwitiya', 'tritiya', 'chaturthi', 'panchami',
              'shasthi', 'saptami', 'ashtami', 'navami', 'dashami',
              'ekadashi', 'dwadashi', 'triyodashi', 'chaturdashi']


def get_tithi(moon_long, sun_long):
    """
    Find's tithi for given moon longitude and sun longitude
    Parameters
    ----------
    moon_long: tuple(degree, minute, secoonds)
    sun_long: tuple(degree, minute, secoonds)
    Returns
    -------
    tuple, (tithi, paksha)
    """
    dl = utils.diff_long(moon_long, sun_long)
    t = int(dl // math.radians(12))
    # print(f"tithi(numeric): {t}")
    if t <= 13:
        res_t = TITHI_NAME[t]
        paksha = 'shukla'
        return (res_t, paksha)
    elif t == 14:
        res_t = 'purnima'
        paksha = 'shukla'
        return (res_t, paksha)
    elif 14 < t < 29:
        res_t = TITHI_NAME[t-15]
        paksha = 'krishna'
        return (res_t, paksha)
    else:
        return ('amavasya', 'krishna')
