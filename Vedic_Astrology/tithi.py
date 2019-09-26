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


def tithi(dl):
    """
    :param dl: difference of longitudes of moon and sun in radians
    :return:tithi, int
    """
    t = dl // math.radians(12)
    # actual tithi is t + 1, python index starts from 0 so adapting accordingly in string_tithi()
    return int(t)


def string_tithi(moon_long, sun_long):
    """
    :param moon_long: tuple(degree, minute, secoonds)
    :param sun_long: tuple(degree, minute, secoonds)
    :return:tithi, paksha
    """
    dl = diff_long(moon_long, sun_long)
    t = tithi(dl)
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


def karna(m, s):
    karna_list = ['kinstughna', 'bava', 'balava', 'kaulava', 'taitila', 'gara', 'vanija', 'vishthi',
                  'bava', 'balava', 'kaulava', 'taitila', 'gara', 'vanija', 'vishthi',
                  'bava', 'balava', 'kaulava', 'taitila', 'gara', 'vanija', 'vishthi',
                  'bava', 'balava', 'kaulava', 'taitila', 'gara', 'vanija', 'vishthi',
                  'bava', 'balava', 'kaulava', 'taitila', 'gara', 'vanija', 'vishthi',
                  'bava', 'balava', 'kaulava', 'taitila', 'gara', 'vanija', 'vishthi',
                  'bava', 'balava', 'kaulava', 'taitila', 'gara', 'vanija', 'vishthi',
                  'bava', 'balava', 'kaulava', 'taitila', 'gara', 'vanija', 'vishthi',
                  'shakuni', 'chatushpada', 'naga']
    d = diff_long(m, s)
    k = d // math.radians(6)
    return karna_list[int(k)]


def yogas(m, s):
    y_list = ['vishkumbha', 'priti', 'ayusmana', 'saubhagya', 'shobhan', 'atiganda', 'sukarma', 'dhriti', 'shula',
              'ganda', 'viridhi', 'dhruva', 'vyaghata', 'harshana', 'vajra', 'sidhi', 'vyatipat', 'variyana',
              'paridha', 'shiva', ' sidha', 'sadhya', 'shubha', 'shukra', 'brahma', 'aindra', 'vaidhriti']
    # add sun and moon longitude
    m_rad = math.radians(dms_to_dd(m))
    s_rad = math.radians(dms_to_dd(s))
    temp_add = m_rad + s_rad
    if temp_add > math.radians(360):
        temp_add -= math.radians(360)
    print(temp_add)

    y = temp_add // 800
    return y_list[int(y)]


def tithi_test():
    moon = [(190, 5, 0), (167, 40, 0), (152, 44, 0), (88, 53, 0)]
    sun = [(156, 7, 0), (178, 49, 0), (177, 49, 0), (304, 4, 0)]
    res = ["tritiya, shukla paksha", "amavasya, krishna paksha", "triyodashi, krishna paksha",
           "triyodashi, shukla paksha"]
    res_karna = ['gara', 'chatushpada', 'vanija', 'kaulava']

    for i in range(len(moon)):
        m = moon[i]
        s = sun[i]
        assert string_tithi(m, s) == res[i]
        assert karna(m, s) == res_karna[i]


def yoga_test():
    m = (323, 32, 0)
    s = (190, 48, 0)
    print(yogas(m, s))


if __name__ == "__main__":
    tithi_test()
    yoga_test()
