import requests
import datetime
import os


USERNAME = "tensor"
TOKEN = os.environ["TOKEN"]

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# 1 - create user on https://pixe.la/
# response = requests.post(url=pixela_endpoint, json=user_params)

# 2 - create graph def
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

graph_config = {
    "id": "graph2",
    "name": "Coding Graph",
    "unit": "h",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# 3 - check your graph
# https://pixe.la/v1/users/tensor/graphs/graph1
# https://pixe.la/v1/users/tensor/graphs/graph2
# https://pixe.la/v1/users/tensor/graphs/graph1.html
# https://pixe.la/v1/users/tensor/graphs/graph2.html

# 4 - post value to graph

today = datetime.datetime.now().strftime("%Y%m%d")
# today = datetime.datetime(year=2022, month=1, day=27).strftime("%Y%m%d")
daily_data = {
    "date": today,
    "quantity": "1"
}

response = requests.post(url=f"{graph_endpoint}/graph2", json=daily_data, headers=headers)


# 5 - update
update_data = {
    "quantity": "4"
}
# response = requests.put(url=f"{graph_endpoint}/graph2/{today}", json=update_data, headers=headers)

# 6 - delete
# response = requests.delete(url=f"{graph_endpoint}/graph2/{today}", json=update_data, headers=headers)

print(response.text)