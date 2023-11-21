import requests
from pprint import pprint


url = "https://jsonplaceholder.typicode.com/posts/1/todos?completed=true"

param = {
    "completed": "true"
}

response = requests.request("GET", url, params=param)

pprint(response.text)


class Todo:
    url = 'https://jsonplaceholder.typicode.com/users/1/todos'

    def get_all(self):
        response = requests.get(self.url)
        return response.text

    def filter(self, parameters):
        response = requests.get(self.url, params=parameters)
        return response.text