from bird import calculate_distance


def get_distance_and_moves(bird_id, birds, time):
    if time == "any":
        bird_by_id = birds.find({"id": bird_id})
    else:
        #bird_by_id = birds.find({"id": bird_id},{"time": "/2019/"})
        bird_by_id = birds.find({"$and": [{"id": bird_id}, {"time":{"$regex": u"" + time +""}}]})
    bird_by_id = list(bird_by_id)
    
    #print(len(bird_by_id))
    total_distance = 0
    used = 0
    print("----------------------------------------------------------")
    print("ID: " + bird_id)
    for i in range(len(bird_by_id) - 1):
        previous = bird_by_id[i]
        actual = bird_by_id[i + 1]
        #print(calculate_distance(previous.get("location"), actual.get("location"))
        actual_distance = calculate_distance(previous.get("location"), actual.get("location"))
        if(actual_distance > 0.001 and (int(previous.get("battery_level")) > int(actual.get("battery_level")))):
            print(str(previous.get("time")) + " " + str(previous.get("battery_level")) + " " + str(actual.get("battery_level")) +" " + str(actual_distance))
            used += 1
            total_distance += actual_distance
    return {"distance":total_distance, "used": used}



def get_total(bird_ids, birds, time):
    total_used = 0
    total_dist = 0
    interator = 0
    bird_ids_len = len(bird_ids)
    for bird_id in bird_ids:
        interator +=1
        dist_movs = get_distance_and_moves(bird_id, birds, time)
        print("ID number : " + str(interator) + " of " + str(bird_ids_len))
        total_used += dist_movs.get("used")
        total_dist += dist_movs.get("distance")
    return {"distance":total_dist, "used": total_used}

def get_birds_ids(birds):
    return list(birds.distinct("id"))

def rank_weather(weather_object):
    rank = 0
    # temperature
    if weather_object.temp > 20:
        rank += 3
    elif weather_object.temp > 10:
        rank += 2
    elif weather_object.temp > 0:
        rank += 1
    # clud_cover
    if weather_object.cloud_cover < 50:
        rank += 1
    # wind
    if weather_object.wind < 8:
        rank += 2
    elif weather_object.wind < 15:
        rank += 1
    # description
    if "Rain" not in weather_object.description:
        rank += 4
    if ("Light Rain" in weather_object.description):
        rank += 1
    return rank
