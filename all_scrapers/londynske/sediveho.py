from all_scrapers.Scraper_Controller import AbstractScraperClass


class Sediveho(AbstractScraperClass):
    def __init__(self):
        self.index_file = "londynske"
        self.url = f'https://www.usedivehovola.com/denni-obedove-menu'
        self.rep = "SEDIVEHOVOLAREPLACEME"
        self.name = "Sediveho"
        self.part_we_want = ['p', {'class': 'font_8'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace("[<p", '<p')
        cleaned_object = cleaned_object.replace("</p>]", '</p>')
        cleaned_object = cleaned_object.replace("</p>, <p", '</p> <p')
        cleaned_object = cleaned_object.replace('<p class="font_8" style="font-size:15px">PONDELI', '<p class="font_8_day" style="font-size:15px">PONDELI')
        cleaned_object = cleaned_object.replace('<p class="font_8" style="font-size:15px">UTERY', '<p class="font_8_day" style="font-size:15px">UTERY')
        cleaned_object = cleaned_object.replace('<p class="font_8" style="font-size:15px">STREDA', '<p class="font_8_day" style="font-size:15px">STREDA')
        cleaned_object = cleaned_object.replace('<p class="font_8" style="font-size:15px"> STREDA', '<p class="font_8_day" style="font-size:15px">STREDA')
        cleaned_object = cleaned_object.replace('<p class="font_8" style="font-size:15px">CTVRTEK', '<p class="font_8_day" style="font-size:15px">CTVRTEK')
        cleaned_object = cleaned_object.replace('<p class="font_8" style="font-size:15px"> CTVRTEK', '<p class="font_8_day" style="font-size:15px">CTVRTEK')
        cleaned_object = cleaned_object.replace('<p class="font_8" style="font-size:15px">PATEK', '<p class="font_8_day" style="font-size:15px">PATEK')

        return cleaned_object


Sediveho().do_scraping()
