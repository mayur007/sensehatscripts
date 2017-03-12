from sense_hat import SenseHat
from time import sleep, time, strftime
from random import randint
import pyowm

owm = pyowm.OWM('5e82ea9b7cd0986bc9f3e3d2823af8eb')

no_rain = [78, 47, 47]
rain = [73, 107, 240]
current = [73, 245, 108]

sense = SenseHat()

def check_rain():
    #get weather from owm
    forecasts = owm.daily_forecast("Cheltenham, uk", 1)
    obs = owm.weather_at_place("Cheltenham, uk")
    obs = obs.get_weather()
    if forecasts.will_have_rain():
        return 1,obs
    else:
        return 0,obs
try:
    rain_status, obs = check_rain()
except Exception,e:
    print "cant get forecasts data", e

count = 0

rain_status, obs = check_rain()

while(1):
    try:
        temp = int(sense.get_temperature())
        sense.set_rotation(180) #change display
        #if its goign to rain then blue colour or else red
	if rain_status:
            sense.show_message(str(temp),text_colour=rain)
        else:
            sense.show_message(str(temp),text_colour=no_rain)
        curtime = strftime('%X')
        #after 8pm display every 500 sec
        if int(curtime.split(':')[0]) > 20:
            sense.show_message(obs.get_status(), text_colour=current )
            rain_status, obs = check_rain()
            sleep(500)
        else:
            sleep(4)
            count += 1
            sense.show_message(obs.get_status(), text_colour=current)
            sleep(4)
            if count == 600:
                count = 0
                rain_status, obs = check_rain()
    except Exception, e:
        print "cant read now", curtime
