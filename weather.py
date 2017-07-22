import sys
import requests	
import json


city = input("Enter City Name : ")
f = open("api.txt","r")
api = f.read()
api = api[:-1]

link = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s"%(city,api)

try:

	data = requests.get(link)

	if(data.status_code!=200):
		print("Error " , data.status_code)
		sys.exit()
	else:
		json_data = json.loads(data.text)
		print("#### Weather Report ####\n")
		print("City Name : ",json_data['name'])
		print("Weather : ",json_data['weather'][0]['description'])
		print("Min Temp. : ",json_data['main']['temp_min']-273.15," Celcius")
		print("Max Temp. : ",json_data['main']['temp_max']-273.15," Celcius")
		print("Wind Speed : ",json_data['wind']['speed']," km/hr")
		print("Clouds : ",json_data['clouds']['all'],"%")
except:
	print("Try after 10 minutes")		

