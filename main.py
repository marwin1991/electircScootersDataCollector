import json
import requests
import uuid
import pymongo
import operator

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
        'radius': 100
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
    r = requests.get(url=url, params=params, headers=headers)
    print(r.status_code)

    return r.json().get("birds")


def sort_scooters_by_distance(birds_repository):
    return sorted(birds_repository.items(), key=operator.itemgetter(1).total_distance)


if __name__ == "__main__":
    birds_repository = {}
    token = 'eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJjODVhNmQ1Zi1jY2U2LTQ3MmYtYmI4Mi02ZTA4NWJiYTBkODAiLCJuYmYiOjE1NzEyMDM4ODIsImV4cCI6MTU3MTI5MDI4MiwiYXVkIjoiYmlyZC5zZXJ2aWNlcyIsImlzcyI6ImJpcmQuYXV0aCIsImlhdCI6MTU3MTIwMzg4Miwicm9sZXMiOlsiVVNFUiJdLCJhcHAiOiI3YjhlZDk1NS02ZTNhLTRlZWMtYmEyMC04OGFmOWQ3YWVhNzYiLCJ2ZXIiOiIwLjAuMiJ9.ItBs1y3W-XBqkroqxMz0Vk68aAieIACCmCingQTf5yvvOeXVKUGvRcn9tpvUJ6V92rgxusI2ZPKTHtKMRnKE_CR7RFMJEflLaM9HaBEumm4Ric9CVMWk546adjf1m85GrCLbTRjzw5wWUGR_wmLxO0AZ4xjuUM15U_f37vtiJ2JVJfjjhCg3FltUDIWccrFONYlsq5W_LrjmEE2jxqgn5j29aBO-nG_hSpvQwOw3xLMk9pf1l1wiXhxSzF26zAG6oTCp8fxtr7HYUYxOwf7Zg01KOSWik4OxOVF_mn1gA_mPJoRRhUmI_m1jtGS3QvfXKj9OdlbnC_U2gm8Uqd3l7cQ1M-uPQeBOjxU3CwLFyt44UEnFp8GEoauIOyGjQFGpVMdz-zm7uhrjzG2hAAL9ot7lnH2Xh7CX94Q2haBzBtlCzk2Dr01rL4fM_rGjvmL7ysBqw0lw4uuvQTDLl2hU0sw0k-QKK40GXxc-qsmEvwVLdLEBdlYdPpFyvxxD1egw_cMZ4x_acJ-IJY8-E3oAMJLOHSq9VSxyXGK-Vh8CXLkKYkQbAtmNnlUVOSfAecJj6EY4_wfa65r2ydkTY1KiW53E_fZue6V2tlkUGVUSiuhAp3SH9JDk_4Va_D0h6Dm8pIGC5ny0H2i5obWl30XcARh8xreZaCxvmepBcgwoC6k'
    guid = '10752AAB-A214-445C-BCBD-936264AA6251'
    crac_long = 19.944544
    crac_lat = 50.049683
    birds = get_nearby_scooters(token, guid, crac_lat, crac_long)
    for bird in birds:
        birds_repository[bird.get("id")] = (
            Bird(bird.get("id"), bird.get("location"), bird.get("code"), bird.get("model"),
                 bird.get("vehicle_class"), bird.get("captive"), bird.get("battery_level"),
                 bird.get("estimated_range"), bird.get("area_key")))
    for id, bird in birds_repository.items():
        print(bird)
