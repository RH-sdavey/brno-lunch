from all_scrapers.Scraper_Controller import AbstractScraperClass


class Makalu(AbstractScraperClass):
    def __init__(self):
        self.url = f'http://www.nepalska-restaurace-makalu.cz/'
        self.rep = "MAKALUREPLACEME"
        self.name = "Makalu"
        self.part_we_want = ['p', {'': ""}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        split_cleaned_object = cleaned_object.split('<b>')  # horrible, makalus website is not easy
        daily_menus_section = str(split_cleaned_object[2:32])
        cleaned_object = str(daily_menus_section).replace("', '", '')
        cleaned_object = cleaned_object.replace('<span class="cena">', '<span style="margin-left:1em;" class="cena">')
        cleaned_object = cleaned_object.replace('Pondeli</b>', '<p>Pondeli</p>')
        cleaned_object = cleaned_object.replace('</p></p>', '</p>')
        cleaned_object = cleaned_object.replace('<p>Polevka:', '<b>Polevka:</b>')
        cleaned_object = cleaned_object.replace('style="margin-left:1em;', 'style="margin-left:4em;')
        cleaned_object = cleaned_object.replace('<p class="TJden">', '')
        cleaned_object = cleaned_object.replace('<p class="TJden">', '')
        cleaned_object = cleaned_object.replace('<p class="TJden">', '')
        cleaned_object = cleaned_object.replace('<p class="TJden">', '')
        cleaned_object = cleaned_object.replace("['", '')
        cleaned_object = cleaned_object.replace("']", '')
        cleaned_object = cleaned_object.replace(",", '')
        cleaned_object = cleaned_object.replace('<b>', '<b class="makalu_b">')
        cleaned_object = cleaned_object.replace('<p>', '<p class="makalu_p">')
        cleaned_object = cleaned_object.replace('<br/> </p>', '<br/> </p><p class="makalu_p">')
        # TODO SOLVE CLEANING MAKALUS CRAP WEBSITE , GOOD LUCK :D
        return cleaned_object


Makalu().do_scraping()
