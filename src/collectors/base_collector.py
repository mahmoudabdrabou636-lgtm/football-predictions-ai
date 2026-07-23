from abc import ABC, abstractmethod


class BaseCollector(ABC):

    @abstractmethod
    def fetch(self):
        """Fetch data from source"""
        pass

    @abstractmethod
    def save(self, data):
        """Save collected data"""
        pass