from all_scrapers.Scraper_Controller import AbstractScraperClass


class Musilce(AbstractScraperClass):
    def __init__(self):
        self.index_file = "zbrojovka"
        self.url = f'https://www.menicka.cz/5400-restaurace-na-musilce.html#m'
        self.rep = "MUSILCEREPLACEME"
        self.name = "Musilce"
        self.part_we_want = ['div', {'class': 'obsah'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        text_I_dont_want = '''
<ul class="socialni">
<li><a class="tisk" href="tisk.php?restaurace=5400" target="_new">Vytisknout</a></li>
<li><a class="pozvatnaobed" href="https://www.menicka.cz/api/pozvankanaobed/?restaurace=5400">Pozvat na obed</a></li>
<li><a class="zasilani" href="https://www.menicka.cz/api/zasilanimenu/?add=5400">Odebirat menu</a></li>
<li><a class="facebook" href="http://www.facebook.com/sharer.php?u=http://www.menicka.cz/5400-restaurace-na-musilce.html" target="_new">Sdilet na Facebooku</a></li>
<div class="clear"></div>
</ul>'''
        cleaned_object = cleaned_object.replace(text_I_dont_want, '')
        cleaned_object = cleaned_object.replace('<div class="nadpis">', '<br/><div style="color:red" class="nadpis">')
        cleaned_object = cleaned_object.replace('class="jidlo"', 'style="list-style: none" class="jidomusilce"')
        return cleaned_object


Musilce().do_scraping()
