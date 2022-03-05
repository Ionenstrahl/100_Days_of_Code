import requests
import os


#This class is responsible retrieving and updating user data
class UserManager:
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/a916ef37053dea9c5c195212ab91a921/flightPrices/users"
        self.sheety_auth = {"Authorization": f"Bearer {os.environ['SECRET']}"}

    def get_user_data(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_auth)
        data = response.json()
        data_structured = [{"first_name": user["firstName"],
                           "last_name": user["lastName"],
                           "email": user["email"]}
                          for user in data["users"]]
        return data_structured

    def get_mails(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_auth)
        mails = [user["email"] for user in response.json()["users"]]
        return mails

    def create_new_user(self, user):
        requests.post(url=self.sheety_endpoint, json=user, headers=self.sheety_auth)

    def retrieve_user_data_by_input(self):

        print("Welcome to Jonas's Flight Club \n"
              "We find the best flight deals and email you.")

        first_name = input("What's your first name?\n")
        last_name = input("What's your last name?\n")

        email = "1"
        verification_mail = "2"
        while email != verification_mail:
            if email == "1":
                email = input("What's your email?\n")
            else:
                email = input("Emails do not match. Please try again!\n")
            verification_mail = input("Please verify and type again\n")
        print("Welcome to the club!")

        user = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }

        return user
