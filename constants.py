mode = ["FDD", "TDD"]

#modulation : number of bits per symbol
modulation = {
    "QPSK": 2,
    "16QAM": 4,
    "64QAM": 6
}
bandwidth = {
    "1.4 MHz": 6,
    "3 MHz": 15,
    "5 MHz": 25,
    "10 MHz": 50,
    "15 MHz": 75,
    "20 MHz": 100
}

coding_rate = {
    "QPSK": (0.076, 0.93),
    "16QAM": (0.3, 0.89),
    "64QAM": (0.45, 0.93)
}

antennas = {
    "SISO": 1,
    "2x2 MIMO": 2,
    "4x4 MIMO": 4
}

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