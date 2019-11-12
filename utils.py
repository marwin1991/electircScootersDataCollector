from bird import calculate_distance


def get_total_distance_and_moves(bird_id, birds, time):
    if time == "any":
        bird_by_id = birds.find({"id": bird_id})
    else:
        bird_by_id = birds.find({"id": bird_id, "time": "/{}/".format(time)})
    bird_by_id = list(bird_by_id)
    total_distance = 0
    total_moves = 0

    for i in range(len(bird_by_id) - 1):
        previous = bird_by_id[i]
        actual = bird_by_id[i + 1]
        distance = calculate_distance(previous.get("location"), actual.get("location"))
        total_distance += distance
        if(distance > 0):
            total_moves +=1

    return [total_distance, total_moves]



def get_total_distance(bird_ids, birds, time):
    total = 0
    for bird_id in bird_ids:
        total += get_total_distance_and_moves(bird_id, birds, time)[0]
    return total


def get_total_moves(bird_ids, birds, time):
    total = 0
    for bird_id in bird_ids:
        total += get_total_distance_and_moves(bird_id, birds, time)[1]
    return total

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
