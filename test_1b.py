from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
import haversine


def test_stations_by_distance():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord1 = (1, 1)
    trange = None
    river = "My River"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord1, trange, river, town)
    coord2 = (1000, 1000)
    s2 = MonitoringStation(s_id, m_id, label, coord2, trange, river, town)
    stations = [s1, s2]
    sorted_stations = stations_by_distance(stations, (0,0))

    assert sorted_stations[0][0] is s1

    assert sorted_stations[0][1] == haversine.haversine((0,0), coord1)
