from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

# get list of stations
stations = build_station_list()
update_water_levels(stations)

print(
    "\n".join(
        station.name + " " + str(level)
        for station, level in stations_level_over_threshold(stations, 0.8)
    )
)
