import requests
from lxml import etree
from bs4 import BeautifulSoup

class MedicineInfoScraper:
    def __init__(self, pid):
        self.url = f"https://osakadou.cool/detail/{pid}.html"

    def run(self):
        response = self.get()
        data = self.parse(response)

    def get(self):
        return requests.get(self.url)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        xml = etree.HTML(str(soup))
        name = xml.xpath("//*[@id=\"OS07763\"]")[0].text.strip()
        print(name)