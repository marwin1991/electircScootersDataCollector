import requests
import json
import datetime
import time

from weather_object import WeatherObject


def get_actual_weather():
    response = requests.get(
        "http://api.worldweatheronline.com/premium/v1/weather.ashx?key=257e3f8938e34e31af3120015193110&format=json&q=50.038923,19.915757&data_element=current_conditions")
    json_data = json.loads(response.text)

    dt = datetime.datetime.today()
    current_condition = json_data["data"]["current_condition"][0]
    data = str(dt.year) + ":" + str(dt.month) + ":" + str(dt.day) + ":" + str(current_condition["observation_time"])
    temp = current_condition["temp_C"]
    cloudcover = current_condition["cloudcover"]
    wind = current_condition["windspeedKmph"]
    description = current_condition["weatherDesc"][0]["value"]
    return data, temp, cloudcover, wind, description


if __name__ == "__main__":
    with open("weather_data.txt", "a") as f:
        data, temp, cloudcover, wind, description = get_actual_weather()
        line = str(data) + "\t" + str(temp) + "\t" + str(cloudcover) + "\t" + str(wind) + "\t" + description + "\n"
        print(line)
        f.write(line)
