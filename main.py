import json
import requests
import uuid
import pymongo
import pandas as pd
import gmaps

from bird import Bird

proxies = {
    # "http": "http://192.168.132.10:80",
    # "https": "http://192.168.132.10:80"
}


def get_token(guid):
    url = 'https://api-auth.prod.birdapp.com/api/v1/auth/email'
    headers = {
        'User-Agent': 'Bird/4.56.0 (co.bird.Ride; build:14; iOS 12.4.1) Alamofire/4.56.0',
        'Device-id': guid,
        'Platform': 'ios',
        'App-Version': '4.56.0',
        'Content-Type': 'application/json',
    }

    payload = {
        'email': '4lovel@vvolkov.top',  # https://generator.email/
    }

    r = requests.post(url=url, data=json.dumps(payload), headers=headers)

    token = r

    return token


def get_nearby_scooters(token, guid, lat, long, radius = 1000, speed = -1):
    url = 'https://api.birdapp.com/bird/nearby'
    params = {
        'latitude': lat,
        'longitude': long,
        'radius': radius
    }
    headers = {
        'Authorization': 'Bird {}'.format(token),
        'Device-id': '{}'.format(guid),
        'App-Version': '4.56.0',
        'Location': json.dumps({
            'latitude': lat,
            'longitude': long,
            'altitude': 0,
            'accuracy': 100,
            'speed': speed,
            'heading': -1
        })
    }

    r = requests.get(url=url, params=params, headers=headers, proxies=proxies)
    print('Request status code: ' + str(r.status_code))
    return r.json()
    
    
def get_conf(lat, long):
    
    url = 'https://api.birdapp.com/config/location'

    params = {
        'latitude': lat,
        'longitude': long,
    }
    
    headers = {
        'App-Version': '4.56.0'
    }

    r = requests.get(url=url, params=params, headers=headers, proxies=proxies)
    print('Request status code: ' + str(r.status_code))
    return r.json()
    
def draw_locs(locs):
    return gmaps.symbol_layer(
        locs, 
        fill_color=(242, 0, 255), 
        stroke_color=(242, 0, 255), 
        scale=2
    )


def get_crocow_scooters():
    token = 'eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJjODVhNmQ1Zi1jY2U2LTQ3MmYtYmI4Mi02ZTA4NWJiYTBkODAiLCJuYmYiOjE1NzEyMDM4ODIsImV4cCI6MTU3MTI5MDI4MiwiYXVkIjoiYmlyZC5zZXJ2aWNlcyIsImlzcyI6ImJpcmQuYXV0aCIsImlhdCI6MTU3MTIwMzg4Miwicm9sZXMiOlsiVVNFUiJdLCJhcHAiOiI3YjhlZDk1NS02ZTNhLTRlZWMtYmEyMC04OGFmOWQ3YWVhNzYiLCJ2ZXIiOiIwLjAuMiJ9.ItBs1y3W-XBqkroqxMz0Vk68aAieIACCmCingQTf5yvvOeXVKUGvRcn9tpvUJ6V92rgxusI2ZPKTHtKMRnKE_CR7RFMJEflLaM9HaBEumm4Ric9CVMWk546adjf1m85GrCLbTRjzw5wWUGR_wmLxO0AZ4xjuUM15U_f37vtiJ2JVJfjjhCg3FltUDIWccrFONYlsq5W_LrjmEE2jxqgn5j29aBO-nG_hSpvQwOw3xLMk9pf1l1wiXhxSzF26zAG6oTCp8fxtr7HYUYxOwf7Zg01KOSWik4OxOVF_mn1gA_mPJoRRhUmI_m1jtGS3QvfXKj9OdlbnC_U2gm8Uqd3l7cQ1M-uPQeBOjxU3CwLFyt44UEnFp8GEoauIOyGjQFGpVMdz-zm7uhrjzG2hAAL9ot7lnH2Xh7CX94Q2haBzBtlCzk2Dr01rL4fM_rGjvmL7ysBqw0lw4uuvQTDLl2hU0sw0k-QKK40GXxc-qsmEvwVLdLEBdlYdPpFyvxxD1egw_cMZ4x_acJ-IJY8-E3oAMJLOHSq9VSxyXGK-Vh8CXLkKYkQbAtmNnlUVOSfAecJj6EY4_wfa65r2ydkTY1KiW53E_fZue6V2tlkUGVUSiuhAp3SH9JDk_4Va_D0h6Dm8pIGC5ny0H2i5obWl30XcARh8xreZaCxvmepBcgwoC6k'
    guid = '10752AAB-A214-445C-BCBD-936264AA6251'

    skawina_lat = 49.984524
    skawina_long = 19.843278

    crac_lat = 50.049683
    crac_long = 19.944544

    delta = 0.01

    birds_dic = {}

    interator = 0
    for i in range(6):
        skawina_lat += delta
        for j in range(6):
            print('Getting birds number: ' + str(interator))
            interator +=1
            skawina_long += delta

            print('long: ' + str(skawina_lat) + ' ; lat: ' + str(skawina_long))
            birds = get_nearby_scooters(token, guid, skawina_lat, skawina_long).get("birds")
            print("Got birds: " + str(len(birds)))
            for bird in birds:
                birds_dic[bird.get("id")] = Bird(bird.get("id"), bird.get("location"), bird.get("code"), bird.get("model"),
                                bird.get("vehicle_class"), bird.get("captive"), bird.get("battery_level"),
                                bird.get("estimated_range"), bird.get("area_key"))

    return [ v for v in birds_dic.values() ]









