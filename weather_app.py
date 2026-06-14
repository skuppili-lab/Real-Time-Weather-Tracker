import requests
city=input("enter your city: ")
url=f"https://wttr.in/{city}?format=j1"    
response = requests.get(url).json()
obv_time = response["current_condition"][0]["observation_time"][0]
temp = response["current_condition"][0]["temp_C"]
weather = response["current_condition"][0]["weatherDesc"][0]["value"]
humidity = response["current_condition"][0]["humidity"]
print(f"City: {city}")
print(f"Observation time: {obv_time}")
print(f"Temperature: {temp}") 
print(f"Humidity: {humidity}")
print(f"Weather conditions: {weather}") 