# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(
        self, station_id, measure_id, label, coord, typical_range, river, town
    ):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """
        return false if the typical range is inconsistent,
        e.g. if the lower range is greater tha the upper range
        or if there is no range given
        """
        if self.typical_range is None:
            return False
        if self.typical_range[0] > self.typical_range[1]:
            return False
        return True

    def relative_water_level(self):
        """
        Returns the latest water level as a fraction of the typical range,
        i.e. a ratio of 1.0 corresponds to a level at the typical high
        and a ratio of 0.0 corresponds to a level at the typical low.
        """
        # if inconsistent range or no latest level return none
        if not (self.typical_range_consistent() and self.latest_level):
            return None

        # return value
        return (self.latest_level - self.typical_range[0]) / (
            self.typical_range[1] - self.typical_range[0]
        )


def inconsistent_typical_range_stations(stations):
    """
    return a list of all stations of which the rage is inconsistent,
    inconsistent as defined in typical_range_consistent()
    """
    inconsistent_stations = []
    for station in stations:
        if not station.typical_range_consistent():
            inconsistent_stations.append(station)
    return inconsistent_stations
