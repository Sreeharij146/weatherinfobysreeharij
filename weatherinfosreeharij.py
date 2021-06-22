# -*- coding: utf-8 -*-
"""weatherinfosreeharij.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rMX8bY7BvlcjY7JK9ewJzTQukkTYzUfg
"""

import requests,sys

from datetime import datetime

api_key = 'be4019569318f4adb52a3fa857ca049f'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

original_stdout = sys.stdout
with open("weatherinfo.txt", "w") as output_file:
  sys.stdout=output_file
  print ("-------------------------------------------------------------")
  print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
  print ("-------------------------------------------------------------")
  print ("Current temperature is: {:.2f} deg C".format(temp_city))
  print ("Current weather desc  :",weather_desc)
  print ("Current Humidity      :",hmdt, '%')
  print ("Current wind speed    :",wind_spd ,'kmph')

sys.stdout = original_stdout

print("The output is written in weatherinfo.txt")