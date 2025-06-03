mode = ["FDD", "TDD"]

# modulation : number of bits per symbol
modulation = {"QPSK": 2, "16-QAM": 4, "64-QAM": 6, "256-QAM": 8}
bandwidth = {
    "1.4 MHz": 6,
    "3 MHz": 15,
    "5 MHz": 25,
    "10 MHz": 50,
    "15 MHz": 75,
    "20 MHz": 100,
}

# coding_rate = {"QPSK": (0.076, 0.93), "16QAM": (0.3, 0.89), "64QAM": (0.45, 0.93)}

SISO = "SISO"
MIMO_2x2 = "2x2 MIMO"
MIMO_4x4 = "4x4 MIMO"
MIMO_8x8 = "8x8 MIMO"

antennas = {SISO: 1, MIMO_2x2: 2, MIMO_4x4: 4, MIMO_8x8: 8}

tdd_uplink_downlink_conf = {
    "DSUUUDSUUU": {"downlink": 2, "uplink": 6, "special": 2},
    "DSUUDDSUUD": {"downlink": 4, "uplink": 4, "special": 2},
    "DSUDDDSUDD": {"downlink": 6, "uplink": 2, "special": 2},
    "DSUUUDDDDD": {"downlink": 6, "uplink": 3, "special": 1},
    "DSUUDDDDDD": {"downlink": 7, "uplink": 2, "special": 1},
    "DSUDDDDDDD": {"downlink": 9, "uplink": 1, "special": 1},
    "DSUUUDSUUD": {"downlink": 3, "uplink": 5, "special": 2},
}

tdd_special_subframe_conf = {
    14: {
    "3 DwPTS symbols, 1 UpPTS symbol": {"downlink": 3, "uplink": 1, "gp": 10},
    "9 DwPTS symbols, 1 UpPTS symbol": {"downlink": 9, "uplink": 1, "gp": 4},
    "10 DwPTS symbols, 1 UpPTS symbol": {"downlink": 10, "uplink": 1, "gp": 3},
    "11 DwPTS symbols, 1 UpPTS symbol": {"downlink": 11, "uplink": 1, "gp": 2},
    "12 DwPTS symbols, 1 UpPTS symbol": {"downlink": 12, "uplink": 1, "gp": 1},
    "3 DwPTS symbols, 2 UpPTS symbol": {"downlink": 3, "uplink": 2, "gp": 9},
    "9 DwPTS symbols, 2 UpPTS symbol": {"downlink": 9, "uplink": 2, "gp": 3},
    "10 DwPTS symbols, 2 UpPTS symbol": {"downlink": 10, "uplink": 2, "gp": 2},
    "11 DwPTS symbols, 2 UpPTS symbol": {"downlink": 11, "uplink": 2, "gp": 1},
    "6 DwPTS symbols, 2 UpPTS symbol": {"downlink": 6, "uplink": 2, "gp": 6}},
    12: {
    "3 DwPTS symbols, 1 UpPTS symbol": {"downlink": 3, "uplink": 1, "gp": 8},
    "8 DwPTS symbols, 1 UpPTS symbol": {"downlink": 8, "uplink": 1, "gp": 3},
    "3 DwPTS symbols, 2 UpPTS symbol": {"downlink": 3, "uplink": 2, "gp": 7},
    "6 DwPTS symbols, 2 UpPTS symbol": {"downlink": 6, "uplink": 2, "gp": 4},
    "9 DwPTS symbols, 2 UpPTS symbol": {"downlink": 9, "uplink": 2, "gp": 1},
    "2 DwPTS symbols, 2 UpPTS symbol": {"downlink": 2, "uplink": 2, "gp": 8},
    }
}


coding_rate_basic_cp = {
    "0": 0.07,
    "1": 0.12,
    "2": 0.18,
    "3": 0.29,
    "4": 0.32,
    "5": 0.15,
    "6": 0.22,
    "7": 0.20,
    "8": 0.25,
    "9": 0.28,
    "10": 0.16,
    "11": 0.22,
    "12": 0.26,
    "13": 0.30,
    "14": 0.35,
    "15": 0.38,
    "16": 0.42,
    "17": 0.44,
    "18": 0.50,
    "19": 0.55,
    "20": 0.57,
    "21": 0.60,
    "22": 0.65,
    "23": 0.67,
    "24": 0.70,
    "25": 0.72,
    "26": 0.74,
    "27": 0.75,
}

coding_rate_extended_cp = {
    "0": 0.08,
    "1": 0.13,
    "2": 0.21,
    "3": 0.33,
    "4": 0.35,
    "5": 0.17,
    "6": 0.25,
    "7": 0.23,
    "8": 0.29,
    "9": 0.32,
    "10": 0.19,
    "11": 0.26,
    "12": 0.31,
    "13": 0.34,
    "14": 0.39,
    "15": 0.43,
    "16": 0.47,
    "17": 0.50,
    "18": 0.55,
    "19": 0.58,
    "20": 0.61,
    "21": 0.64,
    "22": 0.68,
    "23": 0.71,
    "24": 0.73,
    "25": 0.76,
    "26": 0.79,
    "27": 0.80,
}


MCS = {
    "0":  {"modulation": modulation["QPSK"],     12: coding_rate_extended_cp["0"],  14: coding_rate_basic_cp["0"]},
    "1":  {"modulation": modulation["QPSK"],     12: coding_rate_extended_cp["1"],  14: coding_rate_basic_cp["1"]},
    "2":  {"modulation": modulation["QPSK"],     12: coding_rate_extended_cp["2"],  14: coding_rate_basic_cp["2"]},
    "3":  {"modulation": modulation["QPSK"],     12: coding_rate_extended_cp["3"],  14: coding_rate_basic_cp["3"]},
    "4":  {"modulation": modulation["QPSK"],     12: coding_rate_extended_cp["4"],  14: coding_rate_basic_cp["4"]},
    "5":  {"modulation": modulation["16-QAM"],   12: coding_rate_extended_cp["5"],  14: coding_rate_basic_cp["5"]},
    "6":  {"modulation": modulation["16-QAM"],   12: coding_rate_extended_cp["6"],  14: coding_rate_basic_cp["6"]},
    "7":  {"modulation": modulation["16-QAM"],   12: coding_rate_extended_cp["7"],  14: coding_rate_basic_cp["7"]},
    "8":  {"modulation": modulation["16-QAM"],   12: coding_rate_extended_cp["8"],  14: coding_rate_basic_cp["8"]},
    "9":  {"modulation": modulation["16-QAM"],   12: coding_rate_extended_cp["9"],  14: coding_rate_basic_cp["9"]},
    "10": {"modulation": modulation["64-QAM"],   12: coding_rate_extended_cp["10"], 14: coding_rate_basic_cp["10"]},
    "11": {"modulation": modulation["64-QAM"],   12: coding_rate_extended_cp["11"], 14: coding_rate_basic_cp["11"]},
    "12": {"modulation": modulation["64-QAM"],   12: coding_rate_extended_cp["12"], 14: coding_rate_basic_cp["12"]},
    "13": {"modulation": modulation["64-QAM"],   12: coding_rate_extended_cp["13"], 14: coding_rate_basic_cp["13"]},
    "14": {"modulation": modulation["64-QAM"],   12: coding_rate_extended_cp["14"], 14: coding_rate_basic_cp["14"]},
    "15": {"modulation": modulation["64-QAM"],   12: coding_rate_extended_cp["15"], 14: coding_rate_basic_cp["15"]},
    "16": {"modulation": modulation["64-QAM"],   12: coding_rate_extended_cp["16"], 14: coding_rate_basic_cp["16"]},
    "17": {"modulation": modulation["64-QAM"],   12: coding_rate_extended_cp["17"], 14: coding_rate_basic_cp["17"]},
    "18": {"modulation": modulation["64-QAM"],   12: coding_rate_extended_cp["18"], 14: coding_rate_basic_cp["18"]},
    "19": {"modulation": modulation["256-QAM"],  12: coding_rate_extended_cp["19"], 14: coding_rate_basic_cp["19"]},
    "20": {"modulation": modulation["256-QAM"],  12: coding_rate_extended_cp["20"], 14: coding_rate_basic_cp["20"]},
    "21": {"modulation": modulation["256-QAM"],  12: coding_rate_extended_cp["21"], 14: coding_rate_basic_cp["21"]},
    "22": {"modulation": modulation["256-QAM"],  12: coding_rate_extended_cp["22"], 14: coding_rate_basic_cp["22"]},
    "23": {"modulation": modulation["256-QAM"],  12: coding_rate_extended_cp["23"], 14: coding_rate_basic_cp["23"]},
    "24": {"modulation": modulation["256-QAM"],  12: coding_rate_extended_cp["24"], 14: coding_rate_basic_cp["24"]},
    "25": {"modulation": modulation["256-QAM"],  12: coding_rate_extended_cp["25"], 14: coding_rate_basic_cp["25"]},
    "26": {"modulation": modulation["256-QAM"],  12: coding_rate_extended_cp["26"], 14: coding_rate_basic_cp["26"]},
    "27": {"modulation": modulation["256-QAM"],  12: coding_rate_extended_cp["27"], 14: coding_rate_basic_cp["27"]}
}


OVERHEAD = {
    "FDD": {
        SISO: 0.21, 
        MIMO_2x2: 0.24, 
        MIMO_4x4: 0.27,
        MIMO_8x8: 0.31
    },
    "TDD": {
        SISO: 0.21,             #random value tutaj
        MIMO_2x2: 0.24, 
        MIMO_4x4: 0.27,
        MIMO_8x8: 0.31
    }
}
