from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

# get list of stations
stations = build_station_list()
update_water_levels(stations)

print("\n".join(station.name + " " + str(level) for station, level in stations_highest_rel_level(stations, 10)))
