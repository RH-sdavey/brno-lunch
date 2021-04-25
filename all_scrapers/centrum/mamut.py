from all_scrapers.Scraper_Controller import AbstractScraperClass


class Mamut(AbstractScraperClass):
    def __init__(self):
        self.index_file = "centrum"
        self.url = f'https://www.mamut-pub.cz/'
        self.rep = "MAMUTREPLACEME"
        self.name = "Mamut"
        self.part_we_want = ['section', {'id': 'four'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace('<div>Pondeli:', '<br/><hr/><br/><div class="day_mamut">Pondeli:')
        cleaned_object = cleaned_object.replace('<div>Utery:', '<br/><hr/><br/><div class="day_mamut">Utery:')
        cleaned_object = cleaned_object.replace('<div>Streda:', '<br/><hr/><br/><div class="day_mamut">Streda:')
        cleaned_object = cleaned_object.replace('<div>Ctvrtek:', '<br/><hr/><br/><div class="day_mamut">Ctrvrtek:')
        cleaned_object = cleaned_object.replace('<div>Patek:', '<br/><hr/><br/><div class="day_mamut">Patek:')
        cleaned_object = cleaned_object.replace('<span style="white-space:pre"> </span>', '')
        cleaned_object = cleaned_object.replace('<div><strong>', '<div><strong class="day_mamut">')
        return cleaned_object


Mamut().do_scraping()
