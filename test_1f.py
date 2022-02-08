from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_typical_range_consistent():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (1, 1)
    river = "My River"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, [1, 2], river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, [2, 1], river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, None, river, town)

    assert s1.typical_range_consistent()
    assert not s2.typical_range_consistent()
    assert not s3.typical_range_consistent()


def test_inconsistent_typical_range_stations():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (1, 1)
    river = "My River"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, [1, 2], river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, [2, 1], river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, None, river, town)

    stations = [s1, s2, s3]

    incosistent = inconsistent_typical_range_stations(stations)

    assert s1 not in incosistent
    assert s2 in incosistent
    assert s3 in incosistent
