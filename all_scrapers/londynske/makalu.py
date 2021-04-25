from all_scrapers.Scraper_Controller import AbstractScraperClass


class Makalu(AbstractScraperClass):
    def __init__(self):
        self.index_file = "londynske"
        self.url = f'http://www.nepalska-restaurace-makalu.cz/'
        self.rep = "MAKALUREPLACEME"
        self.name = "Makalu"
        self.part_we_want = ['p', {'': ""}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        split_cleaned_object = cleaned_object.split('<b>')  # horrible, makalus website is not easy
        daily_menus_section = str(split_cleaned_object[2:34])
        cleaned_object = str(daily_menus_section).replace("', '", '')
        cleaned_object = cleaned_object.replace('<span class="cena">', '<span style="margin-left:1em;" class="cena">')
        cleaned_object = cleaned_object.replace('Pondeli</b>', '<p>Pondeli</p>')
        cleaned_object = cleaned_object.replace('</p></p>', '</p>')
        cleaned_object = cleaned_object.replace('<p>Polevka:', '<b>Polevka:</b>')
        cleaned_object = cleaned_object.replace('style="margin-left:1em;', 'style="margin-left:4em;')
        cleaned_object = cleaned_object.replace('<p class="TJden">', '')
        cleaned_object = cleaned_object.replace(' Utery', '')
        cleaned_object = cleaned_object.replace(' Ctvrtek', '')
        cleaned_object = cleaned_object.replace('<br/>Ctvrtek', '<br/><br/><p class="makalu_day">Ctvrtek</p>')
        cleaned_object = cleaned_object.replace('<br/>Utery', '<br/><br/><p class="makalu_day">Utery</p>')
        cleaned_object = cleaned_object.replace('<br/>Patek', '<br/><br/><p class="makalu_day">Patek</p>')
        cleaned_object = cleaned_object.replace(' Patek', '')
        cleaned_object = cleaned_object.replace("['", '')
        cleaned_object = cleaned_object.replace("']", '')
        cleaned_object = cleaned_object.replace(",", '')
        cleaned_object = cleaned_object.replace('<b>', '<b class="makalu_soup">')
        cleaned_object = cleaned_object.replace('<p>', '<p class="makalu_day">')
        cleaned_object = cleaned_object.replace('<br/> </p>', '<br/> </p><p class="makalu_day">')
        return cleaned_object


Makalu().do_scraping()
