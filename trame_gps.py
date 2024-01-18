from NMEA0183 import NMEA0183

serial_location = 'COM6'
#serial_location = '/dev/ttyUSB0'
serial_baudrate = 4800
serial_timeout = 10


try:
    NMEA0183=NMEA0183()
except:
    print("error using recuperationdonne")
#Provides the required serial device info
nmea = NMEA0183(serial_location,serial_baudrate,serial_timeout)

#Starts the serial connection
nmea.start()

#Checks if there is a valid connection
if nmea.exit == False:
    print("connection")
   
   #More info on data names below
   #Different data types require different devices...obviously...
   #Some examples...
   
   #GPS data
    print(nmea.data_gps['lat'])
    print (nmea.data_gps['lon'])
    print (nmea.data_gps['utc'])
    """
   #Depth data
    print(nmea.data_depth['feet'])
   
   #Weather data
    print (nmea.data_weather['wind_angle'])
    print (nmea.data_weather['water_temp'])
   
   #Rudder data
    print (nmea.data_rudder['stbd_angle'])
   
    #Quit the NMEA connection
    nmea.quit()
"""
else:
    print('No connection!')