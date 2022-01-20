import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit


def plot_water_levels(station, dates, levels):
    """
    displays a plot of the water level data against time for a station
    """
    plt.plot(dates, levels, label="Current Data")
    plt.hlines(station.typical_range,
               min(dates),
               max(dates),
               linestyles="dashed",
               label="Typical Range")

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title("{}, {}".format(station.name, station.town), )
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    plt.plot(dates, levels, label="Current Data")
    poly, d0 = polyfit(dates, levels, p)
    plt.plot(dates, poly(dates - d0))
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title("{}, {}".format(station.name, station.town), )
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()
