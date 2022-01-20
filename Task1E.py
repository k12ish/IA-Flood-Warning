from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()
    selected_stations = rivers_by_station_number(stations, 9)

    print(selected_stations)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
