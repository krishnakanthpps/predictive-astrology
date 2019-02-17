# Basic Components of Muhurta

import math


def dms_to_dd(degrees):
    """
    :param degrees: tuple(d,m,s)
    :return:decimal degrees
    """
    deg, min, sec = degrees
    dd = deg + (min/60) + (sec / (60 * 60))
    return dd


def tithi(moon_long, sun_long):
    """
    :param moon_long: tuple(degree, minute, secoonds)
    :param sun_long: tuple(degree, minute, secoonds)
    :return:tithi, paksha
    """
    m_rad = math.radians(dms_to_dd(moon_long))
    # print(m_rad)
    s_rad = math.radians(dms_to_dd(sun_long))
    # print(s_rad)
    if m_rad > s_rad:
        t = ((m_rad - s_rad) // math.radians(12))
    else:
        m_rad += math.radians(360)
        t = ((m_rad - s_rad) // math.radians(12))

    t = int(t)
    # print(f"tithi(numeric): {t}")
    tithi_name = ['pratipada', 'dwitiya', 'tritiya', 'chaturthi', 'panchami', 'shasthi', 'saptami', 'ashtami',
                  'navami', 'dashami', 'ekadashi', 'dwadashi', 'triyodashi', 'chaturdashi']
    if t <= 13:
        return f"{tithi_name[t]}, shukla paksha"
    elif t == 14:
        return f"purnima, shukla paksha"
    elif 14 < t < 29:
        return f"{tithi_name[t-15]}, krishna paksha"
    else:
        return f"amavasya, krishna paksha"


def tithi_test():
    moon = [(190, 5, 0), (167, 40, 0), (152, 44, 0), (88, 53, 0)]
    sun = [(156, 7, 0), (178, 49, 0), (177, 49, 0), (304, 4, 0)]
    res = ["tritiya, shukla paksha", "amavasya, krishna paksha", "triyodashi, krishna paksha",
           "triyodashi, shukla paksha"]

    for i in range(len(moon)):
        m = moon[i]
        s = sun[i]
        assert tithi(m, s) == res[i]


if __name__ == "__main__":
    tithi_test()
