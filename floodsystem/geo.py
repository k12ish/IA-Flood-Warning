# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine
from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    """
    Given a list of station objects and a coordinate p,
    return a list of tuples, where distance is the distance of the station from the coordinate p
    """
    return sorted_by_key([(station, haversine(p, station.coord))
                          for station in stations], 1)
