from all_scrapers.Scraper_Controller import AbstractScraperClass


class Taste(AbstractScraperClass):
    def __init__(self):
        self.url = f'https://www.taste-of-india.cz/#daily-menu'
        self.rep = "TASTEREPLACEME"
        self.name = "Taste_of_india"
        self.part_we_want = ['ul', {'class': 'daily-menu'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        return cleaned_object

Taste().do_scraping()


