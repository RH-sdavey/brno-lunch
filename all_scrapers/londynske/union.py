from all_scrapers.Scraper_Controller import AbstractScraperClass


class Union(AbstractScraperClass):
    def __init__(self):
        self.index_file = "londynske"
        self.url = f'http://www.restauraceunion.cz/denni-menu/'
        self.rep = "UNIONREPLACEME"
        self.name = "Union"
        self.part_we_want = ['div', {'class': "entry-content"}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace('font-size: medium', 'font-size: 1em')
        return cleaned_object


Union().do_scraping()
