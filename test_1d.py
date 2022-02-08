from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.station import MonitoringStation


def test_rivers_with_stations():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (1, 1)
    trange = None
    river1 = "My River 1"
    river2 = "My River 2"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river2, town)
    stations = [s1, s2]

    rivers = rivers_with_station(stations)

    assert len(rivers) == 2

    assert river1 in rivers
    assert river2 in rivers


def test_stations_by_river():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (1, 1)
    trange = None
    river1 = "My River 1"
    river2 = "My River 2"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river2, town)
    stations = [s1, s2]

    rivers_to_stations = stations_by_river(stations)

    assert rivers_to_stations["My River 1"][0] is s1
    assert rivers_to_stations["My River 2"][0] is s2
