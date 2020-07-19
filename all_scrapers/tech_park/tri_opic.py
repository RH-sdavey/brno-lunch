from all_scrapers.Scraper_Controller import AbstractScraperClass


class TriOpice(AbstractScraperClass):
    def __init__(self):
        self.url = f'http://www.u3opic.cz/denni-menu/'
        self.rep = "OPICEREPLACEME"
        self.name = "Opice"
        self.part_we_want = ['div', {'class': 'menu-items'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        return cleaned_object


TriOpice().do_scraping()
