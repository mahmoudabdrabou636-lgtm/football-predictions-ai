import requests

from .base_collector import BaseCollector


class FootballDataCollector(BaseCollector):

    def __init__(self):
        self.base_url = ""

    def fetch(self):
        print("Fetching football data...")
        return []

    def save(self, data):
        print(f"Saving {len(data)} records...")