import matplotlib
import numpy as np


def polyfit(dates, levels, p):
    """
    given the water level time history (dates, levels) for a station,
    compute least-squares fit of a polynomial of degree p to water level data
    """
    assert len(dates) == len(levels)
    assert len(dates) > 0

    x = matplotlib.dates.date2num(dates)
    # keep 'x' fairly central about zero using average
    d0 = sum(x) / len(x)
    coeff = np.polyfit(x - d0, levels, p)
    poly = np.poly1d(coeff)
    return poly, d0
