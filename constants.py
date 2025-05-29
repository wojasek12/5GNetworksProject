mode = ["FDD", "TDD"]

# modulation : number of bits per symbol
modulation = {"QPSK": 2, "16-QAM": 4, "64-QAM": 6, "256-QAM": 6}
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
    "DSUUUDDDDD": {"downlink": 7, "uplink": 2, "special": 1},
    "DSUUDDDDDD": {"downlink": 8, "uplink": 1, "special": 1},
    "DSUDDDDDDD": {"downlink": 9, "uplink": 0, "special": 1},
    "DSUUUDSUUD": {"downlink": 3, "uplink": 5, "special": 2},
}

tdd_special_subframe_conf = {
    "3 DwPTS symbols, 1 UpPTS symbol": {"downlink": 3, "uplink": 1, "gp": 10},
    "9 DwPTS symbols, 1 UpPTS symbol": {"downlink": 9, "uplink": 1, "gp": 4},
    "10 DwPTS symbols, 1 UpPTS symbol": {"downlink": 10, "uplink": 1, "gp": 3},
    "11 DwPTS symbols, 1 UpPTS symbol": {"downlink": 11, "uplink": 1, "gp": 2},
    "12 DwPTS symbols, 1 UpPTS symbol": {"downlink": 12, "uplink": 1, "gp": 1},
    "3 DwPTS symbols, 2 UpPTS symbol": {"downlink": 3, "uplink": 2, "gp": 9},
    "9 DwPTS symbols, 2 UpPTS symbol": {"downlink": 9, "uplink": 2, "gp": 3},
    "10 DwPTS symbols, 2 UpPTS symbol": {"downlink": 10, "uplink": 2, "gp": 2},
    "11 DwPTS symbols, 2 UpPTS symbol": {"downlink": 11, "uplink": 2, "gp": 1},
    "6 DwPTS symbols, 2 UpPTS symbol": {"downlink": 6, "uplink": 2, "gp": 6},
}


coding_rate = {
    "0": 0.0762,
    "1": 0.1172,
    "2": 0.1885,
    "3": 0.3008,
    "4": 0.4385,
    "5": 0.6016,
    "6": 0.7402,
    "7": 0.2422,
    "8": 0.3164,
    "9": 0.3818,
    "10": 0.4805,
    "11": 0.6016,
    "12": 0.3047,
    "13": 0.4014,
    "14": 0.4551,
    "15": 0.5508,
    "16": 0.6465,
    "17": 0.7539,
    "18": 0.8184,
    "28": 0.7500,
}


MCS = {
    "0": [modulation["QPSK"], coding_rate["0"]],
    "1": [modulation["QPSK"], coding_rate["1"]],
    "2": [modulation["QPSK"], coding_rate["2"]],
    "3": [modulation["QPSK"], coding_rate["3"]],
    "4": [modulation["QPSK"], coding_rate["4"]],
    "5": [modulation["QPSK"], coding_rate["5"]],
    "6": [modulation["QPSK"], coding_rate["6"]],
    "7": [modulation["16-QAM"], coding_rate["7"]],
    "8": [modulation["16-QAM"], coding_rate["8"]],
    "9": [modulation["16-QAM"], coding_rate["9"]],
    "10": [modulation["16-QAM"], coding_rate["10"]],
    "11": [modulation["16-QAM"], coding_rate["11"]],
    "12": [modulation["64-QAM"], coding_rate["12"]],
    "13": [modulation["64-QAM"], coding_rate["13"]],
    "14": [modulation["64-QAM"], coding_rate["14"]],
    "15": [modulation["64-QAM"], coding_rate["15"]],
    "16": [modulation["64-QAM"], coding_rate["16"]],
    "17": [modulation["64-QAM"], coding_rate["17"]],
    "18": [modulation["64-QAM"], coding_rate["18"]],
    "28": [modulation["256-QAM"], coding_rate["28"]],
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
