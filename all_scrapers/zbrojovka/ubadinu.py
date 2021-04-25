from all_scrapers.Scraper_Controller import AbstractScraperClass


class UBadinu(AbstractScraperClass):
    def __init__(self):
        self.index_file = "zbrojovka"
        self.url = f'http://www.ubadinu.cz/denni-menu-1.html'
        self.rep = "BADINUREPLACEME"
        self.name = "Badinu"
        self.part_we_want = ['div', {'class': 'divgalerie'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        return cleaned_object


UBadinu().do_scraping()
