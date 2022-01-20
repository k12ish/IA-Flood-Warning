from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()
    sorted_stations = stations_by_distance(stations, (52.2053, 0.1218))

    print("Ten closest:")
    print([(s.name, s.town, d) for (s, d) in sorted_stations[:10]])
    print("Ten furthest:")
    print([(s.name, s.town, d) for (s, d) in sorted_stations[-10:]])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
