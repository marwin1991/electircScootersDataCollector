import pymongo

from weather_object import WeatherObject
from utils import rank_weather, get_total, get_birds_ids
import numpy as np
import matplotlib.pyplot as plt


def plot_weather(file):
    days_ = ["2019-10-31", "2019-11-1", "2019-11-2", "2019-11-3", "2019-11-4", "2019-11-5", "2019-11-6", "2019-11-7"]
    days = dict({})
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split("\t")
            print(line)
            day = "-".join(line[0].split(":")[:3])
            weather_object = WeatherObject(line[0], int(line[1]), int(line[2]), int(line[3]), line[4])
            if (day in days.keys()):
                days[day].append(weather_object)
            else:
                days[day] = list([weather_object])

    y = []
    for key, values in days.items():
        ranks = []
        for value in values:
            ranks.append(rank_weather(value))
        y.append(np.mean(ranks))

    print(y)
    x = [i for i in range(len(y))]

    plt.plot(x, y)
    plt.ylabel("Ranks")
    plt.xlabel("Number of day")
    plt.xticks(np.arange(len(days)), [day_[5:] for day_ in days_])
    plt.title("Weather rank")
    plt.show()


def plot_weather_attribute(file, attribute):
    days_ = ["2019-10-31", "2019-11-1", "2019-11-2", "2019-11-3", "2019-11-4", "2019-11-5", "2019-11-6", "2019-11-7"]
    days = dict({})
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split("\t")
            print(line)
            day = "-".join(line[0].split(":")[:3])
            if (attribute == "temp"):
                weather_object = int(line[1])
            elif (attribute == "cloud"):
                weather_object = int(line[2])
            else:
                weather_object = int(line[3])
            if (day in days.keys()):
                days[day].append(weather_object)
            else:
                days[day] = list([weather_object])

        y = []
        for key, values in days.items():
            y.append(np.mean(values))

        print(y)

        x = [i for i in range(len(y))]

        plt.plot(x, y)
        plt.ylabel(attribute)
        plt.xlabel("Day")
        plt.xticks(np.arange(len(days)), [day_[5:] for day_ in days_])
        plt.title("Weather : " + attribute)
        plt.show()


def plot_birds_distance_by_days(birds, birds_ids):
    days = ["2019-10-31", "2019-11-1", "2019-11-2", "2019-11-3", "2019-11-4", "2019-11-5", "2019-11-6"]
    x = [i + 1 for i in range(len(days))]
    y = [get_total(birds_ids, birds, days[i])["distance"] for i in range(len(days))]
    plt.plot(x, y)
    plt.ylabel("Total distance")
    plt.xlabel("Number of day")
    plt.title("")
    plt.xticks(np.arange(len(days)), [day[5:] for day in days])
    plt.show()


def plot_birds_distance_by_hours(birds, birds_ids):
    hours = ["00:", "01:", "02:", "03:", "04:", "05:", "06:", "07:", "08:", "09:"
                                                                            "10:", "11:", "12:", "13:", "14:", "15:",
             "16:", "17:", "18:", "19:"
                                  "20:", "21:", "22:", "23:"]
    x = [i + 1 for i in range(len(hours))]
    y = [get_total(birds_ids, birds, hours[i])["distance"] for i in range(len(hours))]
    plt.plot(x, y)
    plt.ylabel("Total distance")
    plt.xlabel("Hour")
    plt.title("")
    plt.xticks(np.arange(len(hours)), hours)
    plt.show()


def calculate_correlation(data1, data2):
    from scipy.stats import pearsonr
    corr, _ = pearsonr(data1, data2)
    print('Pearsons correlation: %.3f' % corr)


if __name__ == "__main__":
    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # mydb = myclient["db"]
    # birds = mydb["electric_scooters"]
    # birds_ids = get_birds_ids(birds)
    # plot_birds_distance_by_days(birds, birds_ids)
    # plot_weather("weather_data.txt")
    # plot_weather_attribute("weather_data.txt", "temp")
    # plot_weather_attribute("weather_data.txt", "wind")
    # plot_weather_attribute("weather_data.txt", "cloud")

    overall = [7.0, 6.714285714285714, 6.357142857142857, 7.5, 7.25]
    temp = [3.2, 0.0, 8.857142857142858, 13.875, 8.5]
    wind = [8.4, 8.571428571428571, 4.142857142857143, 9.875, 9.75, 1.6666666666666667, 9.466666666666667,
            3.5714285714285716]
    cloud = [0.0, 7.142857142857143, 55.357142857142854, 28.125, 6.25, 58.333333333333336, 31.666666666666668,
             7.142857142857143]


    distance = [25.905349799639755, 35.010145078839216, 31.553070234036657, 37.28301612505923, 19.733514645098232]
    used = [1398, 1216, 1136, 981, 842]
#calculate_correlation(overall, temp)

#calculate_correlation(overall, wind)

#calculate_correlation(overall, cloud)

  #  calculate_correlation(used, overall[:-3])

   # calculate_correlation(used, temp[:-3])

   # calculate_correlation(used, cloud[:-3])

   # calculate_correlation(used, wind[:-3])

#calculate_correlation(distance, overall[:-3])
#calculate_correlation(distance, temp[:-3])
#calculate_correlation(distance, cloud[:-3])
#calculate_correlation(distance, wind[:-3])

#calculate_correlation(temp, used)

plot

