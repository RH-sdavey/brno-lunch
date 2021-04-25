from all_scrapers.Scraper_Controller import AbstractScraperClass


class CharliesSquare(AbstractScraperClass):
    def __init__(self):
        self.index_file = "centrum"
        self.url = f'https://www.charliessquare.cz/menu/'
        self.rep = "CHARLIESSQUAREREPLACEME"
        self.name = "Charlies"
        self.part_we_want = ['div', {'class': 'entry-content'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace('<th class="table-title"', '<th class="table-title"')
        cleaned_object = cleaned_object.replace('</th>', '</th><tr><td></td></tr>')
        cleaned_object = cleaned_object.replace('colspan="2"', 'colspan="1"')
        cleaned_object = cleaned_object.replace('<th class="table-title"', '<br/><hr/><br/><th class="table-title"')
        return cleaned_object


CharliesSquare().do_scraping()
