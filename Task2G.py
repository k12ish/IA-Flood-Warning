# rank all stations based on risk level

import matplotlib.dates

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import predict_future_level
from floodsystem.datafetcher import fetch_measure_levels

stations = build_station_list()
update_water_levels(stations)


def risk_level(station):
    try:
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=3)
        )
        level_tommorow = predict_future_level(dates, levels)[1]
        realtive_level_tommorow = (level_tommorow - station.typical_range[0]) / (
            station.typical_range[1] - station.typical_range[0]
        )
    except:
        print("something happened")
        realtive_level_tommorow = 1

    current_water_level = station.relative_water_level() or 1

    # if already flooded, eg water level more the double typical, rank severe
    if current_water_level > 2:
        return "Severe"
    # if extraperlated will flood within time X make severe
    elif realtive_level_tommorow > 1.9:
        return "Severe"
    # if extrapolated will flood within time Y make high
    elif realtive_level_tommorow > 1.5:
        return "High"
    elif current_water_level > 1.6:
        return "High"
    elif current_water_level > 1.4:
        return "Moderate"
    else:
        return "Low"


for station in stations:
    print("Risk Level for", station.name, "is", risk_level(station))
