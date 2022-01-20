# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    """Requirements for Task 2E"""

    stations = build_station_list()
    update_water_levels(stations)
    station = stations_highest_rel_level(stations, 1)[0][0]
    dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=10))
    plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
