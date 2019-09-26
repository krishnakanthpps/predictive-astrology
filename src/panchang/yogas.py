"""Calculate yogas"""

import math
import utils


YOGAS_LIST = ['vishkumbha', 'priti', 'ayusmana', 'saubhagya', 'shobhan',
              'atiganda', 'sukarma', 'dhriti', 'shula', 'ganda', 'viridhi',
              'dhruva', 'vyaghata', 'harshana', 'vajra', 'sidhi', 'vyatipat',
              'variyana', 'paridha', 'shiva', ' sidha', 'sadhya', 'shubha',
              'shukra', 'brahma', 'aindra', 'vaidhriti']


def yogas(moon_long, sun_long):
    # add sun and moon longitude
    m_rad = math.radians(utils.dms_to_dd(moon_long))
    s_rad = math.radians(utils.dms_to_dd(sun_long))
    temp_add = m_rad + s_rad
    if temp_add > math.radians(360):
        temp_add -= math.radians(360)
    print(temp_add)

    y = temp_add // 800
    return YOGAS_LIST[int(y)]


if __name__ == '__main__':
    m_long = (192, 37, 29)
    s_long = (5, 30, 37)
    print(f"Yogas: {yogas(m_long, s_long)}")
