import requests

API_KEY = "f1a863209189eccbe8d935810dd0eef6"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Please enter the name of the city: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]['description']
    print("Weather in " + str(city) + " is : "+weather)
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Temperature in " + str(city) + " is: "+str(temperature))

else:
    print("Error")
