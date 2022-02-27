# rank all stations based on risk level

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)

risk_levels = []

for station in stations:
    # if already flooded, eg water level more the double typical, rank severe
    if station.relative_water_level() > 2:
        risk_levels.append([station, "Severe"])
    # if extraperlated will flood within time X make severe
    elif False:
        risk_levels.append([station, "Severe"])
        #TODO
    # if extrapolated will flood within time Y make high
    elif False:
        risk_levels.append([station, "High"])
        #TODO
    elif station.relative_water_level() > 1.6:
        risk_levels.append([station, "High"])
    elif station.relative_water_level() > 1.4:
        risk_levels.append([station, "Moderate"])
    else:
        risk_levels.append([station, "Low"])