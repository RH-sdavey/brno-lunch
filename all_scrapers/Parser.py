import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, url):
        self.url = url
        self.weekly_menus = []
        self.html_object = self.make_beautiful_soup_object(self.url)

    def make_beautiful_soup_object(self, url):
        page = requests.get(url)
        data = page.content
        return BeautifulSoup(data, 'html.parser')

    @staticmethod
    def get_element(soup, tag_data):
        if isinstance(tag_data, list):
            return soup.find(tag_data[0], attrs=tag_data[1])
        else:
            return soup.find(tag_data)

    @staticmethod
    def get_all_elements(soup, tag_data):
        if isinstance(tag_data, list):
            return soup.find_all(tag_data[0], attrs=tag_data[1])
        else:
            return soup.find_all(tag_data)

    def add_menu(self, menu):
        self.weekly_menus.append(menu)

    def print(self):
        for menu in self.weekly_menus:
            print(f"*** {menu.date} ***")

            print("--- Soups ---")

            for item in menu.soups:
                print(f"{item.text} - {item.price}")

            print("--- Meals ---")

            for item in menu.meals:
                print(f"{item.text} - {item.price}")