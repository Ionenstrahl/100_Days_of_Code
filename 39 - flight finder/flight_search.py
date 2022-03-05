import requests
import datetime
import os


class FlightSearch:
    # This class is responsible for talking to the Flight Search API: https://tequila.kiwi.com/

    def __init__(self):
        self.departure = "50.93-6.95-300km"  # around cologne
        self.adults = "2"
        self.adult_hold_bag = "1,1"
        self.flights_in_days = 180
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 20

        self.API_KEY = os.environ["KEY"]
        self.BASE_PATH = " https://tequila-api.kiwi.com"
        self.END_POINT = "/v2/search"
        self.header = {"apikey": self.API_KEY}

    def search_flight_deals(self, vacation_data):
        print("search_flight_deals call")
        today = datetime.date.today().strftime("%d/%m/%Y")
        flights_in_days = (datetime.date.today() + datetime.timedelta(days=self.flights_in_days)).strftime("%d/%m/%Y")
        results = []
        for destination in vacation_data:
            params = {
                "fly_from": self.departure,
                "fly_to": destination["iata_code"],
                "date_from": today,
                "date_to": flights_in_days,
                "nights_in_dst_from": self.nights_in_dst_from,
                "nights_in_dst_to": self.nights_in_dst_to,
                "flight_type": "round",
                "adults": self.adults,
                "adult_hold_bag": self.adult_hold_bag,
                "curr": "EUR",
                "price_to": destination["max_price"],
                "sort": "price",
                "limit": 1
            }
            print(f"waiting for response for {destination['iata_code']}...")
            response = requests.get(url=self.BASE_PATH+self.END_POINT, params=params, headers=self.header)
            print(response.json())
            results.append(response.json())
        return results
