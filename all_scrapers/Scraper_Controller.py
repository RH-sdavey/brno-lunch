import datetime
import os

import requests
from bs4 import BeautifulSoup
import unidecode
from abc import ABC


class AbstractScraperClass(ABC):
    """
    """
    def __init__(self, name, url, rep, part_we_want):
        print(f"START --->[ {name} ]---->: ", end=" ")
        self.name = name
        self.url = url
        self.rep = rep
        self.index_file = "../../pages/londynske.html"
        self.part_we_want = part_we_want
        self.html_tag_we_want = self.part_we_want[0]
        self.html_selector_we_want = self.part_we_want[1]
        self.chars_we_hate = ['[', ']']
        self.soup_object = self.get_soup_object()

    def get_soup_object(self):
        try:
            page = requests.get(self.url)
            data = page.content
            soup = BeautifulSoup(data, 'html.parser')
        except:
            print("Soup: Error, ", end=' ')
            raise Exception
        else:
            print("Soup: OK, ", end=' ')
        return soup

    def get_part_we_want_from_soup_object(self):
        html_tag = self.part_we_want[0]
        html_attr_selector = self.part_we_want[1]
        desired_part = self.soup_object.find_all(html_tag, attrs=html_attr_selector)
        return unidecode.unidecode(str(desired_part))

    def do_remove_outer_brackets(self):
        desired_part = self.get_part_we_want_from_soup_object()
        for char in self.chars_we_hate:
            desired_part = str(desired_part).replace(char, '')

        return desired_part

    def do_replacing_in_html_file(self):
        """
        """
        try:
            with open(self.index_file, 'r+') as file:
                file_contents = file.read()
                file.seek(0)
                replace_string = file_contents.replace(self.rep, self.do_individual_cleanup())
                file.write(replace_string)
                file.truncate()
        except:
            print("REPLACEME: Error, ", end=' ')
            raise Exception
        else:
            print("REPLACEME: OK, ", end=' ')

    def do_scraping(self):
        self.do_replacing_in_html_file()
        print('DONE')

    def do_individual_cleanup(self):
        cleaned_object = self.do_remove_outer_brackets()
        cleaned_object = self.do_cleanup_html(cleaned_object)
        return cleaned_object

    @staticmethod
    def get_today_as_a_number():
        today_as_a_number = int(datetime.datetime.today().weekday())
        if int(today_as_a_number) not in range(0, 5):  # Not Mon - Fri
            today_as_a_number = 4  # Display Friday
        return today_as_a_number
