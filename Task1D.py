from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station

# get set of all rivers
river_set = rivers_with_station(build_station_list())

print(str(len(river_set)) + " stations. First 10 - " + ", ".join(sorted(river_set)[:10]))