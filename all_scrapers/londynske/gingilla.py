from all_scrapers.Scraper_Controller import AbstractScraperClass


class Gingilla(AbstractScraperClass):
    def __init__(self):
        self.url = f'https://gingilla.cz/cz-poledni-menu'
        self.rep = "GINGILLAREPLACEME"
        self.name = "Gingilla"
        self.part_we_want = ['div', {'class': "grid4column"}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace('Cely tyden', '')
        cleaned_object = cleaned_object.replace('href="cz-poledni-menu?tyden=7"', 'href="#page-home"')
        cleaned_object = cleaned_object.replace('class="grid4column lastcolumn" style="text-align:right;"', '')
        cleaned_object = cleaned_object.replace('<h6>', '<h4>')
        return cleaned_object


Gingilla().do_scraping()
