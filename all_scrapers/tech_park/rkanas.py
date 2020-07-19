from all_scrapers.Scraper_Controller import AbstractScraperClass


class RKanas(AbstractScraperClass):
    def __init__(self):
        self.url = f'http://www.kanas.cz/stranka/jidelna'
        self.rep = "RKANASREPLACEME"
        self.name = "RKanas"
        self.part_we_want = ['div', {'id': 'tab1'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        return cleaned_object

RKanas().do_scraping()
