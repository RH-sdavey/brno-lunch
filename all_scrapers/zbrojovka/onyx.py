from all_scrapers.Scraper_Controller import AbstractScraperClass


class Onyx(AbstractScraperClass):
    def __init__(self):
        self.index_file = "zbrojovka"
        self.url = f'https://www.menicka.cz/6722-restobar-onyx.html#m'
        self.rep = "ONYXREPLACEME"
        self.name = "Onyx"
        self.part_we_want = ['div', {'class': 'menicka'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        text_i_dont_want = '''
<li style="list-style: none" class="jidloonyx">
<div class="polozka"><span class="poradi">5. </span>POZOR: V zajmu zkvalitnovani sluzeb pro nase zakazniky jsme rozsirili oblasti rozvozu a moznosti zpusobu platby pri rozvozu o platbu kartou Mastercard, VISA a stravenkovou kartu firmy Sodexo. </div>
<div class="clear"></div>
</li>
<li style="list-style: none" class="jidloonyx">
<div class="polozka"><span class="poradi">6. </span>Muzete tedy stale od 9. 30 hod. volat Vase objednavky na tel. cisla 602412978, 777600983. Jidlo Vam radi zabalime a ve zvoleny cas nachystame k odneseni, nebo Vam ho primo dovezeme. </div>
<div class="clear"></div>
</li>
<li style="list-style: none" class="jidloonyx">
<div class="polozka"><span class="poradi">7. </span>Moznost dovozu jidla nabizime, pokud hodnota objednavky presahne 250, - Kc a misto dodani se nachazi v mestske casti Brno - Zidenice, Malomerice, Obrany, Husovice, Cernovice, Julianov, Zabrdovice a Vi</div>
<div class="clear"></div>
</li>
<li style="list-style: none" class="jidloonyx">
<div class="polozka"><span class="poradi">8. </span>Restobar Onyx / Facebook</div>
<div class="clear"></div>
</li>
<li style="list-style: none" class="jidloonyx">
<div class="polozka"><span class="poradi">9. </span>www. zomato. cz/restauraceonyx</div>
<div class="clear"></div>
</li>
<li style="list-style: none" class="jidloonyx">
<div class="polozka"><span class="poradi">10. </span>Restaurace Onyx / Google. cz </div>
<div class="clear"></div>
</li>'''
        cleaned_object = cleaned_object.split('</div>, <div class="menicka">')[0]
        cleaned_object = cleaned_object.replace('class="jidlo"', 'style="list-style: none" class="jidloonyx"')
        cleaned_object = cleaned_object.replace(text_i_dont_want, '')
        cleaned_object = cleaned_object.replace('</ul>', '</ul> </div>')
        # cleaned_object = cleaned_object.replace('"polozka">Polevka', '"polozka" style="color:red">Polevka')
        cleaned_object = cleaned_object.replace('li class="polevka"', 'li class="onyx_polevka"')
        cleaned_object = cleaned_object.replace('<div class="polozka"><span class="poradi">4.', '<div style="color:red" class="polozka_onyx"><span class="poradi">4.')
        cleaned_object = cleaned_object.replace('<div class="polozka"><span class="poradi">5.', '<div style="color:red" class="polozka_onyx"><span class="poradi">5.')
        cleaned_object = cleaned_object.replace('<div class="polozka"><span class="poradi">6.', '<div style="color:red" class="polozka_onyx"><span class="poradi">6.')
        cleaned_object = cleaned_object.replace('<div class="polozka"><span class="poradi">7.', '<div style="color:red" class="polozka_onyx"><span class="poradi">7.')

        return cleaned_object


Onyx().do_scraping()
