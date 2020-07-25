from all_scrapers.Parser import Parser
from models.DailyMenu import DailyMenu
from models.Meal import Meal


class Sediveho(Parser):
    def __init__(self):
        self.url = 'https://www.usedivehovola.com/denni-obedove-menu'
        super(Sediveho, self).__init__(self.url)

        self.content_tag_data = ['div', {'id': 'comp-k7bm7v9k'}]
        self.item_tag_data = 'p'
        self.days = ['PONDĚLÍ', 'ÚTERÝ', 'STŘEDA', 'ČTVRTEK', 'PÁTEK']


    def process(self):
        content = self.get_element(self.html_object, self.content_tag_data)

        if content is not None:
            elements = self.get_all_elements(content, self.item_tag_data)

            daily_menu = DailyMenu()

            for element in elements:
                meal = Meal()

                text = element.get_text().strip()

                if text.split(' ')[0] in self.days:
                    data = text.split('–')
                    daily_menu.set_date(data[0].strip())

                    meal.set_text(data[1].strip())

                    daily_menu.soups.append(meal)
                elif len(text.strip()) > 0:
                    pos = text[0:-3].rfind(' ')

                    meal_name = text[0:pos].strip()
                    if meal_name[-1:] == '-':
                        meal_name = meal_name[:-1].strip()

                    meal.set_text(meal_name)
                    meal.set_price(text[pos:].strip())

                    daily_menu.meals.append(meal)
                elif len(daily_menu.meals) > 0:
                    self.weekly_menus.append(daily_menu)
                    daily_menu = DailyMenu()

            if len(daily_menu.meals) > 0:
                self.weekly_menus.append(daily_menu)

        self.print()


Sediveho().process()