from all_scrapers.Scraper_Controller import AbstractScraperClass


class Varna(AbstractScraperClass):
    def __init__(self):
        self.url = f'https://restauraceportoriko.cz/denni-menu/'
        self.rep = "PORTORIKOREPLACEME"
        self.name = 'Portoriko'
        self.part_we_want = ['div', {'class': 'print-not'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace("Tisk", "")
        return cleaned_object


Varna().do_scraping()
