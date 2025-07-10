from abc import ABC, abstractmethod

class BaseSpider(ABC):
    def __init__(self, name):
        self.name = name
        print(f"Spider '{self.name}' starting.")

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def parse_data(self, raw_data):
        pass

    def scrape(self):
        print(f"Starting the scraper with '{self.name}' spider...")
        raw_data = self.get_data()
        if raw_data:
            print("Got the raw data, parsing...")
            structured_data = self.parse_data(raw_data)
            return structured_data
        else:
            print("It was not possible to obtain the raw data.")
            return []