from all_scrapers.Scraper_Controller import AbstractScraperClass


class Mitrovski(AbstractScraperClass):
    def __init__(self):
        self.index_file = "londynske"
        self.url = f'https://www.mitrovski.cz/menu/'
        self.rep = "MITROVSKIREPLACEME"
        self.name = "Mitrovski"
        self.part_we_want = ['div', {'class': 'b-text-c'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        for item in [',', '=""', '</div><div class="b b-text cf">', '<a name="patek"></a>',
                     '<div class="b-c">', '<div class="ez-c">',
                     '<div class="section-bg-layer section-bg-overlay"></div>',
                     '<div class="section-bg-layer">']:
            cleaned_object = cleaned_object.replace(item, '')
        return cleaned_object


Mitrovski().do_scraping()

