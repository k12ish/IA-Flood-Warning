from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation


def test_rivers_by_station_number():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (1, 1)
    trange = None
    river1 = "My River 1"
    river2 = "My River 2"
    river3 = "My River 3"
    river4 = "My River 4"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river2, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river3, town)
    s5 = MonitoringStation(s_id, m_id, label, coord, trange, river2, town)
    s6 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    s7 = MonitoringStation(s_id, m_id, label, coord, trange, river3, town)
    s8 = MonitoringStation(s_id, m_id, label, coord, trange, river4, town)
    stations = [s1, s2, s3, s4, s5, s6, s7, s8]

    assert len(rivers_by_station_number(stations, 1)) == 1

    river_list = rivers_by_station_number(stations, 2)

    # case where multiple entries with same number in Nth position
    assert len(river_list) == 3

    assert "My River 4" not in [item[0] for item in river_list]

    for river in ["My River 1", "My River 2", "My River 3"]:
        assert river in [item[0] for item in river_list]

