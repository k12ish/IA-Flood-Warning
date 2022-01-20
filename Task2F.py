import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    """Requirements for Task 2E"""

    stations = build_station_list()
    update_water_levels(stations)
    stations_and_rel_level = stations_highest_rel_level(stations, 5)
    for station, _ in stations_and_rel_level:
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=2))
        print(dates, levels)
        plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
