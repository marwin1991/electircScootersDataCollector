
import numpy as np
import matplotlib.pyplot as plt
hours = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09" ,"10", "11", "12",
        "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23" ]


birds = []

birds_by_hour = dict({})
for hour in hours:
        birds_by_hour[hour] = []


print(birds_by_hour)

with open("travels.csv") as f:
        lines = f.readlines()[1:]
        for line in lines:
                line = line.split(",")
                if(line[-2].startswith("2019-11-02")):
                        birds.append(line)
        print(len(birds))


for bird in birds:
        distance = float(bird[2])
        time = bird[-2]
        time = time.split(" ")[1]
        time = time.split(":")
        birds_by_hour[time[0]].append(distance)

x = hours
y = [np.std(birds_by_hour[hour]) for hour in hours]
plt.figure(figsize=(10,5))
plt.bar(x, y)
plt.ylabel("Std of traveled distanced on 2019-11-02")
plt.xlabel("Hours")
plt.title("")
plt.show()



