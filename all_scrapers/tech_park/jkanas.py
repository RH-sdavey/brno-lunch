from all_scrapers.Scraper_Controller import AbstractScraperClass


class JKanas(AbstractScraperClass):
    def __init__(self):
        self.url = f'http://www.kanas.cz/stranka/jidelna'
        self.rep = "JKANASREPLACEME"
        self.name = "JKanas"
        self.part_we_want = ['div', {'id': 'tab2'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        return cleaned_object

JKanas().do_scraping()

