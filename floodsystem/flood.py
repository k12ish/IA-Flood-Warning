from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """
    return a sorted list of tuples of (station, relative water level)
    sorted based on water level, descending, and only where water level > tol
    """
    return sorted_by_key(
        [
            (station, station.relative_water_level())
            for station in stations
            if station.relative_water_level() and station.relative_water_level() > tol
        ],
        1,
    )[::-1]


def stations_highest_rel_level(stations, N):
    """
    Returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest.
    The list is sorted in descending order by relative level.
    """
    return sorted_by_key(
        [
            (station, station.relative_water_level())
            for station in stations
            if station.relative_water_level()
        ],
        1,
    )[::-1][:N]
