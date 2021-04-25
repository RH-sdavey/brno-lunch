from all_scrapers.Scraper_Controller import AbstractScraperClass


class Babeta(AbstractScraperClass):
    def __init__(self):
        self.index_file = "londynske"
        self.url = f'http://babeta-rest.cz/#dayfood'
        self.rep = "BABETAREPLACEME"
        self.name = "Babeta"
        self.part_we_want = ['table', {'id': "tablepress-4"}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        return cleaned_object

Babeta().do_scraping()
