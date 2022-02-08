from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation
import haversine


def test_stations_within_radius():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord1 = (1, 1)
    trange = None
    river = "My River"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord1, trange, river, town)
    coord2 = (1, 2)
    s2 = MonitoringStation(s_id, m_id, label, coord2, trange, river, town)
    stations = [s1, s2]
    close_stations = stations_within_radius(stations, (0, 0), haversine.haversine(coord1, (0,0)))

    assert s1 in close_stations

    assert s2 not in close_stations
