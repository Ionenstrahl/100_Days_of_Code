import requests
import os


#This class is responsible for talking to the Google Sheet.
class DataManager:

    def get_sheety_data(self):
        sheety_endpoint = "https://api.sheety.co/a916ef37053dea9c5c195212ab91a921/flightPrices/vacationDestinations"
        sheety_auth = {"Authorization": f"Bearer {os.environ['SECRET']}"}
        response = requests.get(url=sheety_endpoint, headers=sheety_auth)
        data_raw = response.json()
        data_structured = [{"iata_code": destination["iata"], "max_price": destination["maxPrice"]} for destination in data_raw["vacationDestinations"]]
        return data_structured


