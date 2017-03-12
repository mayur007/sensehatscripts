import pyowm

while(1):
  owm = pyowm.OWM('5e82ea9b7cd0986bc9f3e3d2823af8eb')
  forecasts = owm.daily_forecast("Cheltenham, uk", 1)
  obs = owm.weather_at_place("Cheltenham, uk")
  obs = obs.get_weather()

  #forecasts = owm.daily_forecast("Cheltenham, uk", 1)
  print "will it be rainy", forecasts.will_have_rain()
  #forecast = forecasts.get_forecast()
  #for eforecast in forecast:
  #  print "forecast:", eforecast.get_status()

  obs = owm.weather_at_place("Cheltenham, uk")
  obs = obs.get_weather()
  print "observation:", obs.get_status()
