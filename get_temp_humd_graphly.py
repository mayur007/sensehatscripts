import plotly.plotly as py
from plotly.graph_objs import *
from sense_hat import SenseHat
from time import sleep
from datetime import datetime

sense = SenseHat()

#print ("temp:%s C, Humidity:%s %%rH" %(temp,humidity))

py.sign_in("m2r0007", "2itofo4gss")
stream_token = 'wqj6ajmwkz'
trace1 = Scatter(
	x=[],
	y=[],
stream=dict(
	token=stream_token,
	maxpoints=2000
	)
)

layout = Layout(
		title='SenseHat hall temperature'
		)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi hall temp Values')
stream = py.Stream(stream_token)
stream.open()
		
while True:
	temp = sense.get_temperature()
	humidity = sense.get_humidity()
        data = str(temp) + ',' + str(humidity) + ',' + str(datetime.now())
        with open('temperature_log.csv', 'a') as tfile:
            tfile.write(data)
            tfile.write('\n')
        tfile.close()
	stream.write({'x': datetime.now(), 'y': temp})
	sleep(2000) # delay between stream posts
