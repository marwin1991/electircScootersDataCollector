from geopy.distance import geodesic


class Bird:
    def __init__(self, id, location, code, model, vehicle_class, captive, battlery_level, estimated_range, area_key):
        self.id = id
        self.time = None
        self.location = location
        self.code = code
        self.model = model
        self.vehicle_class = vehicle_class
        self.captive = captive
        self.battery_level = battlery_level
        self.estimated_range = estimated_range
        self.area_key = area_key

    def set_new_location(self, new_location):
        self.location = new_location
    
    def set_time(self, time):
        self.time = time

def calculate_distance(old_location, new_location):
    old_location = (old_location.get("latitude"), old_location.get("longitude"))
    new_location = (new_location.get("latitude"), new_location.get("longitude"))
    distance = geodesic(old_location, new_location).kilometers
    return distance

