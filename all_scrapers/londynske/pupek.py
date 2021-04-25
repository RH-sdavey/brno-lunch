from all_scrapers.Scraper_Controller import AbstractScraperClass


class Pupek(AbstractScraperClass):
    def __init__(self):
        self.index_file = "londynske"
        self.url = 'https://www.uhovezihopupku.cz/menu/'
        self.rep = "PUPEKREPLACEME"
        self.name = 'Pupek'
        self.part_we_want = ['table', {'class': 'menu_den'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = str(cleaned_object).replace(
            '<td class="menu_jidlo_poradi"><img class="img_polevka" src="/img/polevka_2.png"/></td>', '')
        cleaned_object = cleaned_object.replace('[<table class="menu_den">',
                                                            '<table class="menu_den">')
        cleaned_object = cleaned_object.replace('</table>, <table', '</table> <table')
        cleaned_object = cleaned_object.replace('</table>]', '</table>')
        cleaned_object = cleaned_object.replace('<td class="menu_jidlo_gramaz"> </td>', '')
        cleaned_object = cleaned_object.replace('menu_jidlo_polevka">', 'menu_jidlo_polevka">POLEVKA:')
        cleaned_object = cleaned_object.replace('<b>', '<b class="b_pupek">')

        # TODO CLEAN UP THE REST OF THE OUTPUT
        return cleaned_object


Pupek().do_scraping()
