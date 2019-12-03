

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

hours = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09" ,"10", "11", "12",
        "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23" ]

locations = ["cen", "agh", "zam", "kaz", "grz", "dwo", "kle"]
locations_indexes = {"cen":0, "agh":1, "zam":2, "kaz":3, "grz":4, "dwo":5, "kle":6}




birds = []

birds_by_hour = dict({})
for hour in hours:
        birds_by_hour[hour] = [0,0,0,0,0,0,0]


print(birds_by_hour)
print("///")

with open("travels.csv") as f:
        lines = f.readlines()[1:]
        for line in lines:
                line = line.split(",")
                if(1==1):
                        birds.append(line)
        print(len(birds))


for bird in birds:
        distance = float(bird[2])
        time = bird[-2]
        location = bird[-3]
        time = time.split(" ")[1]
        time = time.split(":")
        index = locations_indexes[location]
        birds_by_hour[time[0]][index] +=1

def plot_one(i):
        x = locations
        y = birds_by_hour[hours[i]]
        plt.figure(figsize=(10,5))
        plt.bar(x, y)
        plt.ylabel("Bird used in hour : " + hours[i] )
        plt.xlabel("Locations")
        plt.title("")
        plt.show()
#        plt.savefig("locations_hour_" + hours[i])

def plot_all(f):
        plt.bar(locations, birds_by_hour[hours[f]])
        plt.show()

interact(plot_all, f=(0,24,1))




