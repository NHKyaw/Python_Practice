import requests
import json
# C=K−273.15
weather_url = "http://api.openweathermap.org/data/2.5/weather?q=Yangon"
appid = "fa0eb4e1b0754428791eccd199160398"
weather_paramether = {
        "q" : "Yangon",
        "appid" : appid
    }

response = requests.get(weather_url, params=weather_paramether)
data = response.json()
des = data['weather'][0]['description']
temp = data['main']['temp'] - 273.15
city = data['name']
country = data['sys']['country']
# print(json.dumps(data, indent=4))

print (f"Today Temperature in {city},{country} is {temp:.2f} Degree Celcius and it is {des}.")

if des == "light rain":
    print ("Don't forget to bring umbrella.")
elif des == "overcast clouds":
    print ("Woo, Today Weather is so fine. Let's chill out.")
else:
    print ("Please watch the further weather forcasting")
