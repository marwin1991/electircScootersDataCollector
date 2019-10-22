import json
import requests
import uuid
import pymongo
import pandas as pd
import gmaps

from bird import Bird


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


def get_nearby_scooters(token, guid, lat, long):
    url = 'https://api.birdapp.com/bird/nearby'
    params = {
        'latitude': lat,
        'longitude': long,
        'radius': 10000
    }
    headers = {
        'Authorization': 'Bird {}'.format(token),
        'Device-id': '{}'.format(guid),
        'App-Version': '4.41.0',
        'Location': json.dumps({
            'latitude': lat,
            'longitude': long,
            'altitude': 0,
            'accuracy': 100,
            'speed': -1,
            'heading': -1
        })
    }
    
    proxies = {
     "http": "http://192.168.132.10:80",
     "https": "http://192.168.132.10:80"
    }

    r = requests.get(url=url, params=params, headers=headers, proxies=proxies)
    print(r.status_code)

    return r.json().get("birds")
    
    
def get_conf(lat, long):
    
    url = 'https://api.birdapp.com/config/location'

    params = {
        'latitude': lat,
        'longitude': long,
    }
    
    headers = {
        'App-Version': '4.41.0'
    }

    proxies = {
     "http": "http://192.168.132.10:80",
     "https": "http://192.168.132.10:80"
    }

    r = requests.get(url=url, params=params, headers=headers, proxies=proxies)
    print(r.status_code)
    return r.json()
    
def draw_locs(locs):
    return gmaps.symbol_layer(
        locs, 
        fill_color=(242, 0, 255), 
        stroke_color=(242, 0, 255), 
        scale=2
    )









