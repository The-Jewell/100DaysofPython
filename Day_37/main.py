import requests
from datetime import datetime
import token as tk

USERNAME = "thejewell"

GRAPH_ID = "graph1"


# created user account for pixela
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": tk.TOKEN,
    "username": "thejewell",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# create the graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "mi",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": tk.TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# post a pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.00"
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


# update a pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.00"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# delete a pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
