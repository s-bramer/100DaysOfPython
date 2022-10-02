import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME= "pickledsprout"
TOKEN = "mypersonalpixelatoken"
DATE = datetime.now().strftime('%Y%m%d')
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# 1. create a new user
# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

# 2. create a graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)

# print(response.text)

# 3. look at the graph
my_graph_endpoint_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}.html"
#print(my_graph_endpoint_url)

#4. add entry to graph
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_entry_parameters = {
    "date": DATE,
    "quantity": "2",
}

# response = requests.post(url=pixel_endpoint, json=pixel_entry_parameters, headers=headers)
# print(response.text)


#5. update pixel with put
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

pixel_update_parameters = {
    "quantity": "3",
}

# response = requests.put(url=update_pixel_endpoint, json=pixel_update_parameters, headers=headers)
# print(response.text)

#5. remove pixel with delete
response = requests.delete(url=update_pixel_endpoint, json=pixel_update_parameters, headers=headers)
print(response.text)