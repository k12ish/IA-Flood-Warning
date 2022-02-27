import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit


def plot_water_levels(station, dates, levels):
    """
    displays a plot of the water level data against time for a station
    """
    plt.plot(dates, levels, label="Fetched Data")
    plt.hlines(
        station.typical_range,
        min(dates, default=0),
        max(dates, default=0),
        linestyles="dashed",
        label="Typical Range",
    )

    plt.xlabel("date")
    plt.ylabel("water level (m)")
    plt.title("{}, {}".format(station.name, station.town), )
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    plt.plot(dates, levels, label="Fetched Data")
    poly, d0 = polyfit(dates, levels, p)
    plt.plot(dates,
             poly(matplotlib.dates.date2num(dates) - d0),
             label="best fit")
    plt.xlabel("date")
    plt.ylabel("water level (m)")
    plt.title("{}, {}".format(station.name, station.town))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()
