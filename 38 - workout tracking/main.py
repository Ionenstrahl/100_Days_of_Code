import requests
import datetime
import os

text_input = "home workout for 30 mins"

# 1 - setup API credentials for https://developer.nutritionix.com/
APP_ID = os.environ["ID"]
API_KEY = os.environ["KEY"]

# 2 - API call

nutr_endpoint = "https://trackapi.nutritionix.com/"
nutr_method = "v2/natural/exercise"

# text_input = input("what did you do? ")

nutr_params = {
    "query": text_input,
    "gender": "male",
    "weight_kg": 76,
    "height_cm": 180,
    "age": 29
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=nutr_endpoint+nutr_method, json=nutr_params, headers=headers)
data = response.json()

# 3 - config sheety https://dashboard.sheety.co/projects/61dfcb810f9a2e53eaf7ec2d/sheets/workouts

# 4 - post sport data to sheety
current_date = datetime.date.today().strftime("%d-%m-%Y")
current_time = datetime.datetime.now().strftime("%H")

sheety_endpoint = "https://api.sheety.co/a916ef37053dea9c5c195212ab91a921/myWorkouts/workouts"
sheety_auth = {"Authorization": f"Bearer {os.environ['SECRET']}"}

for exercise in data["exercises"]:
    sheety_params = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_auth)
    print(response.text)
