from all_scrapers.Scraper_Controller import AbstractScraperClass


class LiquidBread(AbstractScraperClass):
    def __init__(self):
        self.url = f'http://www.liquidbread.cz/dennimenu/'
        self.rep = "LIQUIDBREADREPLACEME"
        self.name = 'Liquid'
        self.part_we_want = ['p', {'': ''}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = str(cleaned_object).replace(',', '')
        return cleaned_object


LiquidBread().do_scraping()
