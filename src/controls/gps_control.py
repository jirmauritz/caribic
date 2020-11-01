from gps import gps, WATCH_ENABLE, WATCH_NEWSTYLE

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

for i in range(100):
   nx = gpsd.next()
   if nx['class'] == 'TPV':
      print('Class: ', nx['class'])
      latitude = getattr(nx, 'lat', "Unknown")
      longitude = getattr(nx, 'lon', "Unknown")
      print("Your position: lon = " + str(longitude) + ", lat = " + str(latitude))
