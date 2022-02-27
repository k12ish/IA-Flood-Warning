# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list


def run():

    # Build list of stations
    stations = build_station_list()

    # Station name to find
    station_name = "Cam"

    # Find station
    station_cam = None
    for station in stations:
        if station.name == station_name:
            station_cam = station
            break

    # Check that station could be found. Return if not found.
    if not station_cam:
        print("Station {} could not be found".format(station_name))
        return

    # Fetch data over past 2 days
    dt = 2
    dates, levels = fetch_measure_levels(station_cam.measure_id,
                                         dt=datetime.timedelta(days=dt))

    if len(dates) == 0 or len(level):
        print(f"Could not fetch data for station", station_name)

    # Print level history
    for date, level in zip(dates, levels):
        print(date, level)


if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()
