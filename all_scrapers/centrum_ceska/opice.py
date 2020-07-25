from all_scrapers.Scraper_Controller import AbstractScraperClass


class Opice(AbstractScraperClass):
    def __init__(self):
        self.url = f'https://www.pivniopice.cz/'
        self.rep = "OPICEREPLACEME"
        self.name = "Opice"
        self.part_we_want = ['div', {'class': "container"}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        return cleaned_object

Opice().do_scraping()
