from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

# get list of stations
stations = build_station_list()

# get set of all rivers
river_set = rivers_with_station(stations)
print(
    str(len(river_set)) + " stations. First 10 - " + ", ".join(sorted(river_set)[:10])
)

# get dict of rivers to stations
rivers_to_stations = stations_by_river(stations)


# get sorted list of stations on a river
def print_stations_on_river_sorted(river):
    """
    print a sorted list of the stations on a particular river
    """
    print(sorted([station.name for station in rivers_to_stations[river]]))


print_stations_on_river_sorted("River Aire")
print_stations_on_river_sorted("River Cam")
print_stations_on_river_sorted("River Thames")
