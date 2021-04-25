from all_scrapers.Scraper_Controller import AbstractScraperClass


class Svitavska(AbstractScraperClass):
    def __init__(self):
        self.index_file = "zbrojovka"
        self.url = f'http://www.svitavskarychta.cz/tydenni-menu/'
        self.rep = "SVITASKAREPLACEME"
        self.name = "Svitavska"
        self.part_we_want = ['div', {'class': 'entry'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        text_i_dont_want = [
            'Polevka k menu pouze do 15.00 hod.',
            'Denni menu prubezne dovarujeme a podavame do 21.00 hod.',
            'Denni menu podavame take v sobotu a nedeli',
            'Ostatni nabidka jidel a chutovek k pivu a napojum najdete v',
            'odpolednim jidelnim listku ( po 15.00 hod. ) nebo dle aktualni',
            'cerstve nabidky.',
            'Dobrou chut preje kolektiv kuchyne Svitavska Rychta',
            'Pripadne nedostatky hlaste ihned obsluze. Dekujeme.',
            'Alergeny obsazene v jidle a jejich seznam na vyzadani u obsluhy',
            'Na stravenky nevracime',
            'Hmotnost porci masa v syrovem stavu',
            'www.svitavskarychta.cz',
            'wifi: 2018svitavskarychta'
        ]
        for item in text_i_dont_want:
            cleaned_object = cleaned_object.replace(item, '')
        return cleaned_object


Svitavska().do_scraping()
