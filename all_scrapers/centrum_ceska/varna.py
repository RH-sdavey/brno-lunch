from all_scrapers.Scraper_Controller import AbstractScraperClass


class Varna(AbstractScraperClass):
    def __init__(self):
        self.url = f'http://www.restauracevarna.cz/denni-menu/'
        self.rep = "VARNAREPLACEME"
        self.name = "Varna"
        self.part_we_want = ['div', {'id': 'pravy-sloupec-obsah'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        return cleaned_object


Varna().do_scraping()

