import pymongo
from time import gmtime, strftime
import pandas
import gmaps

import time
import sys
from bird import Bird
from main import *
import utils

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["db"]
mycol = mydb["electric_scooters"]


def insert(cur_time, birds_table) :
    for bird in birds_table:
        bird.set_time(cur_time)
        mycol.insert_one(bird.__dict__)
    

if __name__ == "__main__" :
    try:
        cur_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print("Time: " + cur_time)
        birds_table = get_crocow_scooters()
        print("Time: " + cur_time + " Found birds: " + str(len(birds_table)))
        insert(cur_time, birds_table)
        print(utils.get_total_distance("36ab65b0-c0d9-4250-997d-622f214cb871", mycol, "any"))
    except KeyboardInterrupt:
        sys.exit(1)
    except:
        print("Something went wrong")
    print("end")