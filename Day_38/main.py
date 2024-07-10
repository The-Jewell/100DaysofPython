import keys as k
import requests
from datetime import datetime

log_exercise = input("Tell me what Exercise you did: ")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/7ed9231bc06e9cb8bdda37f0e57ddcf9/workoutTracking/workouts"

nutritionix_params = {
    "query": log_exercise
}

nutritionix_headers = {
    "Content-Type": "application/json",
    "x-app-id": k.APP_ID,
    "x-app-key": k.API_KEY
}
sheety_headers = {
    "Authorization": k.SHEETY_BEARER
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    exercise_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        },
    }

    sheet_response = requests.post(sheety_endpoint, json=exercise_data, headers=sheety_headers)
