from all_scrapers.Scraper_Controller import AbstractScraperClass


class Morgal(AbstractScraperClass):
    def __init__(self):
        self.index_file = "centrum"
        self.url = f'https://www.morgal.cz/aktualni-nabidka-jidel'
        self.rep = "MORGALREPLACEME"
        self.name = "Morgal"
        self.part_we_want = ['div', {'class': 'jidlobox'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace('<h2>', '<h4>')
        cleaned_object = cleaned_object.replace('</h2>', '</h4>')
        cleaned_object = cleaned_object.replace('<h4>', '<h4 class="morgal_h4">')
        return cleaned_object

Morgal().do_scraping()
