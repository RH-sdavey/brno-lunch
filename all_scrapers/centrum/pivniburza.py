from all_scrapers.Scraper_Controller import AbstractScraperClass


class Burza(AbstractScraperClass):
    def __init__(self):
        self.index_file = "centrum"
        self.url = f'http://pivniburza.cz/denni-menu/'
        self.rep = "BURZAREPLACEME"
        self.name = "Pivni Burza"
        self.part_we_want = ['div', {'class': 'vc_column-inner'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace('<h4>Pondeli', '<h4 class="burza_day">Pondeli')
        cleaned_object = cleaned_object.replace('<h4>Utery', '<h4 class="burza_day">Utery')
        cleaned_object = cleaned_object.replace('<h4>Streda', '<h4 class="burza_day">Streda')
        cleaned_object = cleaned_object.replace('<h4>Ctvrtek', '<h4 class="burza_day">Ctvrtek')
        cleaned_object = cleaned_object.replace('<h4>Patek', '<h4 class="burza_day">Patek')
        return cleaned_object

Burza().do_scraping()
