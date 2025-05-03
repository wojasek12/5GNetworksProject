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