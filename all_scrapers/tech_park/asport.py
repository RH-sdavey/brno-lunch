from all_scrapers.Scraper_Controller import AbstractScraperClass


class Asport(AbstractScraperClass):
    def __init__(self):
        self.url = f'http://www.a-sporthotel.cz/menu/'
        self.rep = "ASPORTREPLACEME"
        self.name = 'Asport'
        self.part_we_want = ['div', {'class': 'ct-code-block'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        return cleaned_object


Asport().do_scraping()
