import matplotlib
import numpy as np

import matplotlib.dates



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


def predict_future_level(dates, levels):
    """
    given the water level time history (dates, levels) for a station,
    return tuple of future date, water level at thatdate
    """
    assert len(dates) == len(levels)
    assert len(dates) > 0

    x = matplotlib.dates.date2num(dates)
    d0 = sum(x) / len(x)
    coeff = np.polyfit(x - d0, levels, 3)
    poly = np.poly1d(coeff)

    # one day after the most recent day
    future_date = max(x) + 1
    return matplotlib.num2date(future_date), poly(future_date - d0)
