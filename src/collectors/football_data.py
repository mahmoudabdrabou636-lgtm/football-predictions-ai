import requests

from .base_collector import BaseCollector


class FootballDataCollector(BaseCollector):

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.football-data.org/v4"

    def fetch(self):
        headers = {
            "X-Auth-Token": self.api_key
        }

        response = requests.get(
            f"{self.base_url}/matches",
            headers=headers
        )

        if response.status_code == 200:
            return response.json()

        print(f"Error: {response.status_code}")
        return {}

    def save(self, data):
        print("Data received successfully.")