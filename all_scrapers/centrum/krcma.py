from all_scrapers.Scraper_Controller import AbstractScraperClass


class Krcma(AbstractScraperClass):
    def __init__(self):
        self.index_file = "centrum"
        self.url = f'https://stredovekakrcma.cz/denni-menu/'
        self.rep = "KRCMAREPLACEME"
        self.name = "Krcma"
        self.part_we_want = ['div', {'class': 'et_pb_text_inner'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace('<h3><strong>', '<h3><strong class="krcma_day">')
        cleaned_object = cleaned_object.replace('<h3 style="text-align: center;"><strong>', '<h3 style="text-align: center;"><strong class="krcma_day">')
        cleaned_object = cleaned_object.replace(', <div class="et_pb_text_inner">', '<!-- , <div class="et_pb_text_inner">')
        cleaned_object = cleaned_object.replace('nejake otazky!</p></div>', 'nejake otazky!</p></div> -->')
        return cleaned_object


Krcma().do_scraping()
