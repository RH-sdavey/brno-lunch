from all_scrapers.Scraper_Controller import AbstractScraperClass


class Purkynka(AbstractScraperClass):
    def __init__(self):
        self.url = f'http://www.napurkynce.cz/denni-menu/'
        self.rep = "PURKYNKAREPLACEME"
        self.name = "Purkynka"
        self.part_we_want = ['p', {'': ''}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = str(cleaned_object).replace(',', '')
        return cleaned_object


Purkynka().do_scraping()
