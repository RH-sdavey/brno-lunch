import datetime
from all_scrapers.Scraper_Controller import AbstractScraperClass


def get_today():
    today_as_a_number = datetime.datetime.today().weekday()
    if today_as_a_number == 0:  # Mon
        today = 't_pondeli'
    elif today_as_a_number == 1:  # Tues
        today = 't_utery'
    elif today_as_a_number == 2:  # Wed
        today = 't_streda'
    elif today_as_a_number == 3:  # Thurs
        today = 't_ctvrtek'
    elif today_as_a_number == 4:  # Fri
        today = 't_patek'
    elif today_as_a_number == 5:  # Sat
        today = 't_sobota'
    elif today_as_a_number == 6:  # Sun
        today = 't_nedele'
    return today


class Padowetz(AbstractScraperClass):
    def __init__(self):
        self.index_file = "centrum"
        self.url = f'http://www.restaurant-padowetz.cz/poledni-menu.htm'
        self.rep = "PADOWETZREPLACEME"
        self.name = "Padowetz"
        self.part_we_want = ['div', {'id': f'{get_today()}'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace('<img src="images/icons/print_on.png" title="Tisk menu poledniho menu"/>', '')
        cleaned_object = cleaned_object.replace('<img src="../ikony/Polevky.png"/>', '')
        cleaned_object = cleaned_object.replace('<img src="../ikony/Hlavni-chod.png"/>', '')
        cleaned_object = cleaned_object.replace('<img src="../ikony/Napoje-k-menu.png"/>', '')
        return cleaned_object

Padowetz().do_scraping()
