from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
stations = build_station_list()

print(sorted([station.name for station in inconsistent_typical_range_stations(stations)]))