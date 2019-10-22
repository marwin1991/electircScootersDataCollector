
from geopy.distance import geodesic

class Bird:
  def __init__(self, id, location,code, model, vehicle_class,captive, battlery_level,estimated_range,area_key ):
    self.id = id
    self.location = location
    self.code = code
    self.model = model
    self.vehicle_class = vehicle_class
    self.captive = captive
    self.battery_level = battlery_level
    self.estimated_range = estimated_range
    self.area_key = area_key


  def calculate_distance(self, new_location):
    old_location = (self.location.get("latitude"),self.location.get("longitude"))
    new_location = new_location.get("latitude",self.location.get("longitude"))
    return geodesic(old_location, new_location).kilometers



