# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine
from collections import Counter
from bisect import bisect
from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    """
    Given a list of station objects and a coordinate p,
    return a list of tuples, where distance is the distance of the station from the coordinate p
    """
    return sorted_by_key([(station, haversine(p, station.coord))
                          for station in stations], 1)


def stations_within_radius(stations, centre, r):
    """
    returns a list of all stations (type MonitoringStation) within radius r of centre.
    """
    stations_by_dist = stations_by_distance(stations, centre)
    stations = [s for (s, _) in stations_by_dist]
    distances = [d for (_, d) in stations_by_dist]
    return stations[:bisect(distances, r)]


def rivers_with_station(stations):
    """
    Given list of stations, return as set of all the
    rivers names contained within these stations
    """
    return set([station.river for station in stations])


def stations_by_river(stations):
    """
    Given list of stations, return a dict of all the stations on a river
    """
    rivers = {}
    for station in stations:
        if station.river in rivers:
            rivers[station.river].append(station)
        else:
            rivers[station.river] = [station]
    return rivers


def rivers_by_station_number(stations, N):
    """
    determines the N rivers with the greatest number of monitoring stations.
    returns a list of (river name, number of stations) tuples
    """
    count = Counter(s.river for s in stations)
    count_of_nth = count.most_common(N)[-1][1]
    return [(r, c) for (r, c) in count.most_common() if c >= count_of_nth]
