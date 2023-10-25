import requests
import json
import pyttsx3

city = input("Enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=845a0b4fd82d468ca49163146232510&q={city}"
r = requests.get(url)

# print(r.text) (To get full info about wind, updation & other geographic details)

engine = pyttsx3.init()
w_dict = json.loads(r.text)
c_weather = w_dict["current"]["temp_c"]

# Display temperature in the console
print(f"The current weather in {city} is {c_weather} degrees")

# Speak the temperature
engine.say(f"The current weather in {city} is {c_weather} degrees")
engine.runAndWait()