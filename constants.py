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
    "2x2 MIMO": 2
}

tdd_uplink_downlink_conf = {
    "DSUUUDSUUU": 0,
    "DSUUDDSUUD": 1,
    "DSUDDDSUDD": 2,
    "DSUUUDDDDD": 3,
    "DSUUDDDDDD": 4,
    "DSUDDDDDDD": 5,
    "DSUUUDSUUD": 6
}

tdd_special_subframe_conf = {
    "3 DwPTS symbols, 1 UpPTS symbol": 0,
    "9 DwPTS symbols, 1 UpPTS symbol": 1,
    "10 DwPTS symbols, 1 UpPTS symbol": 2,
    "11 DwPTS symbols, 1 UpPTS symbol": 3,
    "12 DwPTS symbols, 1 UpPTS symbol": 4,
    "3 DwPTS symbols, 2 UpPTS symbol": 5,
    "9 DwPTS symbols, 2 UpPTS symbol": 6,
    "10 DwPTS symbols, 2 UpPTS symbol": 7,
    "11 DwPTS symbols, 2 UpPTS symbol": 8,
    "6 DwPTS symbols, 2 UpPTS symbol": 9,
}