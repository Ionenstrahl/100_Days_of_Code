from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user_data import UserManager


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

UserManager = UserManager()
# user = UserManager.retrieve_user_data_by_input()
# UserManager.create_new_user(user)
mails = UserManager.get_mails()

DataManager = DataManager()
vacation_data = DataManager.get_sheety_data()

FlightSearch = FlightSearch()
found_flights = FlightSearch.search_flight_deals(vacation_data)

FlightData = FlightData()
found_flights_structured = FlightData.structure_data(found_flights)

NotificationManager = NotificationManager()
NotificationManager.send_message(found_flights_structured, "console", mails)
