import pymongo

from weather_object import WeatherObject
from utils import rank_weather, get_total_moves, get_total_distance, get_birds_ids
import numpy as np
import matplotlib.pyplot as plt

def plot_weather(file):
    days = dict({})
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split("\t")
            print(line)
            day = "-".join(line[0].split(":")[:3])
            weather_object = WeatherObject(line[0], int(line[1]), int(line[2]), int(line[3]), line[4])
            if(day in days.keys()):
                days[day].append(weather_object)
            else:
                days[day] = list([weather_object])

    y = []
    print(days.items())
    for key, values in days.items():
        ranks = []
        for value in values:
            ranks.append(rank_weather(value))
        y.append(np.mean(ranks))

    x = [i for i in range(len(y))]

    plt.plot(x, y)
    plt.ylabel("Ranks")
    plt.xlabel("Number of day")
    plt.show()


def plot_birds_distance(birds, birds_ids):
    days = ["2019-10-31" , "2019-11:1", "2019-11:2", "2019-11:3", "2019-11:4", "2019-11:5", "any"]
    x = [i+1 for i in range(len(days))]
    y = [get_total_distance(birds_ids, birds, days[i]) for i in range(len(days))]
    plt.plot(x, y)
    plt.ylabel("Total distance")
    plt.xlabel("Number of day")
    plt.show()


if __name__ == "__main__":
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["db"]
    birds = mydb["electric_scooters"]
    birds_ids = get_birds_ids(birds)
    plot_birds_distance(birds, birds_ids)