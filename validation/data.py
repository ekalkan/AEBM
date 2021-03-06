
hazard_x = [
    0.010,
    0.020,
    0.030,
    0.050,
    0.075,
    0.10,
    0.15,
    0.20,
    0.25,
    0.30,
    0.38,
    0.40,
    0.45,
    0.50,
    0.55,
    0.60,
    0.65,
    0.70,
    0.75,
    0.80,
    0.930,
    1.0,
    1.1,
    1.2,
    1.30,
    1.4,
    1.5,
    1.6,
    1.8,
    2.0,
    2.2,
    2.4,
    2.6,
    2.8,
    3.0,
    3.2,
    3.4,
    3.6,
    3.8,
    4.0,
    4.5,
    5.0,
    5.5,
    6.0,
    6.5,
    7.0,
    7.5,
    8.0,
    9.0,
    10.0
]

hazard_y = [
    0.4824,
    0.4836,
    0.4980,
    0.5615,
    0.6765,
    0.7848,
    0.9696,
    1.0827,
    1.1377,
    1.1456,
    1.1399,
    1.1385,
    1.1103,
    1.0850,
    1.0454,
    1.0093,
    0.9761,
    0.9453,
    0.9166,
    0.8905,
    0.8302,
    0.8002,
    0.759,
    0.721,
    0.686,
    0.653,
    0.623,
    0.595,
    0.543,
    0.496,
    0.454,
    0.416,
    0.381,
    0.348,
    0.318,
    0.297,
    0.278,
    0.259,
    0.242,
    0.226,
    0.195,
    0.168,
    0.149,
    0.132,
    0.116,
    0.102,
    0.088,
    0.080,
    0.067,
    0.054,
]

hazard = []
for i in range(len(hazard_x)):
    hazard += [{'x': hazard_x[i], 'y': hazard_y[i]}]

capacity_x = [
    0.00,
    0.00,
    0.00,
    0.00,
    0.00,
    0.00,
    0.00,
    0.00,
    0.00,
    0.00,
    0.94,
    1.07,
    1.40,
    1.77,
    2.17,
    2.62,
    3.11,
    3.65,
    4.22,
    4.83,
    6.57,
    7.60,
    9.20,
    10.95,
    12.85,
    14.90,
    17.11,
    19.46,
    24.64,
    30.41,
    36.80,
    43.80,
    51.40,
    59.61,
    68.43,
    77.86,
    87.90,
    98.54,
    109.79,
    121.65,
    153.97,
    190.09,
    230.00,
    273.72,
    321.24,
    372.57,
    427.69,
    486.62,
    615.88,
    760.34,
    76034.19
]

capacity_y = [
    0.000,
    0.000,
    0.000,
    0.000,
    0.000,
    0.000,
    0.000,
    0.000,
    0.000,
    0.000,
    0.666,
    0.686,
    0.708,
    0.722,
    0.734,
    0.744,
    0.753,
    0.761,
    0.767,
    0.772,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777,
    0.777
]


mag = 7.9
hazard_beta = .4
r_rup = 11.18

demand_check = [
    {'x': .01, 'disp': 0, 'y': 0.4800},
    {'x': .02, 'disp': 0.0020, 'y': 0.4800},
    {'x': .03, 'disp': 0.0040, 'y': 0.4900},
    {'x': .05, 'disp': 0.0130, 'y': 0.5500},
    {'x': .075, 'disp': 0.0360, 'y': 0.6500},
    {'x': .1, 'disp': 0.0720, 'y': 0.7400},
    {'x': .15, 'disp': 0.1950, 'y': 0.8800},
    {'x': .2, 'disp': 0.3800, 'y': 0.9700},
    {'x': .25, 'disp': 0.6200, 'y': 1.0100},
    {'x': .3, 'disp': 0.8960, 'y': 1.0200},
    {'x': .38, 'disp': 1.4240, 'y': 1.0100},
    {'x': .4, 'disp': 1.5780, 'y': 1.0100},
    {'x': .45, 'disp': 1.7280, 'y': 0.8700},
    {'x': .5, 'disp': 1.8200, 'y': 0.7400},
    {'x': .55, 'disp': 2.0180, 'y': 0.6800},
    {'x': .6, 'disp': 2.2000, 'y': 0.6200},
    {'x': .65, 'disp': 2.3630, 'y': 0.5700},
    {'x': .7, 'disp': 2.5020, 'y': 0.5200},
    {'x': .75, 'disp': 2.6170, 'y': 0.4800},
    {'x': .8, 'disp': 2.8480, 'y': 0.4600},
    {'x': .93, 'disp': 3.4400, 'y': 0.4100},
    {'x': 1.0, 'disp': 3.7490, 'y': 0.3800},
    {'x': 1.1, 'disp': 4.2500, 'y': 0.3600},
    {'x': 1.2, 'disp': 4.7470, 'y': 0.3400},
    {'x': 1.3, 'disp': 5.2380, 'y': 0.3200},
    {'x': 1.4, 'disp': 5.7180, 'y': 0.3000},
    {'x': 1.5, 'disp': 6.1840, 'y': 0.2800},
    {'x': 1.6, 'disp': 6.6940, 'y': 0.2700},
    {'x': 1.8, 'disp': 7.6850, 'y': 0.2400},
    {'x': 2.0, 'disp': 8.6220, 'y': 0.2200},
    {'x': 2.2, 'disp': 9.5840, 'y': 0.2000},
   {'x': 2.4, 'disp': 10.4800, 'y': 0.1900},
   {'x': 2.6, 'disp': 11.2970, 'y': 0.1700},
   {'x': 2.8, 'disp': 12.0200, 'y': 0.1600},
   {'x': 3.0, 'disp': 12.6380, 'y': 0.1400},
   {'x': 3.2, 'disp': 13.4900, 'y': 0.1300},
   {'x': 3.4, 'disp': 14.2830, 'y': 0.1300},
   {'x': 3.6, 'disp': 14.9390, 'y': 0.1200},
   {'x': 3.8, 'disp': 15.5150, 'y': 0.1100},
   {'x': 4.0, 'disp': 16.0060, 'y': 0.1000},
   {'x': 4.5, 'disp': 17.4660, 'y': 0.0900},
   {'x': 5.0, 'disp': 18.4930, 'y': 0.0800},
   {'x': 5.5, 'disp': 19.8850, 'y': 0.0700},
   {'x': 6.0, 'disp': 20.9550, 'y': 0.0600},
   {'x': 6.5, 'disp': 21.6650, 'y': 0.0500},
   {'x': 7.0, 'disp': 21.9770, 'y': 0.0500},
   {'x': 7.5, 'disp': 21.9780, 'y': 0.0400},
   {'x': 8.0, 'disp': 23.5220, 'y': 0.0400},
   {'x': 9.0, 'disp': 26.3260, 'y': 0.0300},
   {'x': 10.0, 'disp': 28.1730, 'y': 0.0300}
]