from all_scrapers.Scraper_Controller import AbstractScraperClass


class Tahu(AbstractScraperClass):
    def __init__(self):
        self.index_file = "centrum"
        self.url = f'https://www.na-tahu.cz/cz/page/index.html'
        self.rep = "TAHUREPLACEME"
        self.name = "Na Tahu"
        self.part_we_want = ['div', {'class': 'container'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace('<section class="feature">', '<!-- <section class="feature">')
        cleaned_object = cleaned_object.replace('</div>, <div class="container">', '</div>, <div class="container"> -->')
        cleaned_object = cleaned_object.replace('</section>\n</div>', '</section>\n</div>')
        cleaned_object = cleaned_object.replace('<header class="major"><h3>Kontakt</h3></header>', '<!-- <header class="major"><h3>Kontakt</h3></header> -->')
        cleaned_object = cleaned_object.replace('<p style="text-align: center;">TELEFON: 542 211 570</p>', '<!-- <p style="text-align: center;">TELEFON: 542 211 570</p> -->')
        cleaned_object = cleaned_object.replace('<header class="major"><h3>Facebook</h3></header>', '<!-- <header class="major"><h3>Facebook</h3></header> -->')
        cleaned_object = cleaned_object.replace('<a href="https://cs-cz.facebook.com/RestauraceNaTahu"', '<!-- <a href="https://cs-cz.facebook.com/RestauraceNaTahu" ')
        cleaned_object = cleaned_object.replace('src="/public/content/images/fcb.png" style="width: 200px; height: 78px;"/></a></p>', 'src="/public/content/images/fcb.png" style="width: 200px; height: 78px;"/></a></p> -->')
        cleaned_object = cleaned_object.replace('<div>PONDELI:', '<br/><div>PONDELI:')
        cleaned_object = cleaned_object.replace('<div>UTERY:', '<hr/><br/><div>UTERY:')
        cleaned_object = cleaned_object.replace('<div>STREDA:', '<hr/><br/><div>STREDA:')
        cleaned_object = cleaned_object.replace('<div>CTVRTEK:', '<hr/><br/><div>CTVRTEK:')
        cleaned_object = cleaned_object.replace('<div>PATEK:', '<hr/><br/><div>PATEK:')
        cleaned_object = cleaned_object.replace('<p>PONDELI:', '<p class="tahu_day">PONDELI')
        cleaned_object = cleaned_object.replace('<p>STREDA:', '<p class="tahu_day">STREDA')
        cleaned_object = cleaned_object.replace('<p>PATEK:', '<p class="tahu_day">PATEK')
        return cleaned_object


Tahu().do_scraping()
