from all_scrapers.Scraper_Controller import AbstractScraperClass


class Kone(AbstractScraperClass):
    def __init__(self):
        self.index_file = "zbrojovka"
        self.url = f'http://www.steakhousek1.cz/www/restaurace-menu.php'
        self.rep = "KONEREPLACEME"
        self.name = "k1"
        self.part_we_want = ['article', {'id': 'article'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace('h2', 'h3')
        return cleaned_object


Kone().do_scraping()
