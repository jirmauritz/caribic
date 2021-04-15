from gps import gps, WATCH_ENABLE, WATCH_NEWSTYLE


def gps_data():
    """
    Generator that tracks gps data and yields whenever new lat and lon
    values are available.
    """
    gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
    lat = 0
    lon = 0
    satellites = 0
    tpv = False
    sky = False
    while True:
        nx = gpsd.next()
        if nx['class'] == 'TPV':
            lat = getattr(nx, 'lat', 0)
            lon = getattr(nx, 'lon', 0)
            tpv = True
        elif nx['class'] == 'SKY':
            satellites = len(nx['satellites'])
            sky = True
        if sky and tpv:
            return satellites, lat, lon
        
