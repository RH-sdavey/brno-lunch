from all_scrapers.Scraper_Controller import AbstractScraperClass


class Sediveho(AbstractScraperClass):
    def __init__(self):
        self.url = f'https://www.usedivehovola.com/denni-obedove-menu'
        self.rep = "SEDIVEHOVOLAREPLACEME"
        self.name = "Sediveho"
        self.part_we_want = ['p', {'class': 'font_8'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace("[<p", '<p')
        cleaned_object = cleaned_object.replace("</p>]", '</p>')
        cleaned_object = cleaned_object.replace("</p>, <p", '</p> <p')
        return cleaned_object


Sediveho().do_scraping()
