"""

Simple Weather Forecast
Robocode IT Academy Andijan
Student Salaydinov Nurullo
Used openweathermap
You can create your own api key with subscribe to openweathermap
You Can Add 

"""
import requests
import math

while True:
	city_name = input("Shahar yoki Davlat nomini yozing: ")
	if city_name != "":
		if city_name == "stop":
			break
		else:
			url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=your api key"
			# accepting information as json
			response = requests.get(url).json()
			# rounding information
			country = response["name"]
			weather = response["weather"][0]["main"]
			degree = math.ceil(response["main"]["temp"]-273.15) # change to celcius from kelvin
			speed = response["wind"]["speed"]
			humidity = response["main"]["humidity"]
			sea_level = response["main"]["sea_level"]
			# i translate to my language
			if weather == 'Clouds':
				weather = "Bulutli"
			if weather == 'Clear':
				weather = "Ochiq"
			if weather == 'Snow':
				weather = "Qorli"
			if weather == 'Rainy':
				weather = "Yomg'irli"
			# if you need english delete this ^^^
			print(f"\nDavlat: {country}\nHavo Harorati: {degree}\nHavo: {weather}\nShamol Tezligi: {speed}m/s\nNamlik: {humidity}\nDengiz Sathi: {sea_level}")
	else:
		print("you must write there")
