from scraper.base_spider import BaseSpider
import requests
from bs4 import BeautifulSoup

class OlxSpider(BaseSpider):
    def __init__(self, name):
        super().__init__(name)
    
    def get_data(self):
        pass
    
    def parse_data(self, raw_data):
        pass