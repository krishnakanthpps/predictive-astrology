"""Calculate karnas"""

import math
import sys
sys.path.append("/home/arunkhattri/github/predictive-astrology/src/")
from utilities import utils

KARNA_LIST = ['kinstughna', 'bava', 'balava', 'kaulava', 'taitila', 'gara',
              'vanija', 'vishthi', 'bava', 'balava', 'kaulava', 'taitila',
              'gara', 'vanija', 'vishthi', 'bava', 'balava', 'kaulava',
              'taitila', 'gara', 'vanija', 'vishthi', 'bava', 'balava',
              'kaulava', 'taitila', 'gara', 'vanija', 'vishthi', 'bava',
              'balava', 'kaulava', 'taitila', 'gara', 'vanija', 'vishthi',
              'bava', 'balava', 'kaulava', 'taitila', 'gara', 'vanija',
              'vishthi', 'bava', 'balava', 'kaulava', 'taitila', 'gara',
              'vanija', 'vishthi', 'bava', 'balava', 'kaulava', 'taitila',
              'gara', 'vanija', 'vishthi', 'shakuni', 'chatushpada', 'naga']


def get_karna(moon_long, sun_long):
    """
    params moon_long: Moon longitude in (degree, minute, secoonds)
    params sun_long: Sun longitude in (degree, minute, secoonds)
    Returns karna of the day
    """
    d = utils.diff_long(moon_long, sun_long)
    k = d // math.radians(6)
    return KARNA_LIST[int(k)]


if __name__ == '__main__':
    m_long = (192, 37, 29)
    s_long = (5, 30, 37)
    print(f"Karna: {get_karna(m_long, s_long)}")
