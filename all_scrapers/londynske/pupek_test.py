from all_scrapers.Parser import Parser
from models.DailyMenu import DailyMenu
from models.Meal import Meal


class Pupek(Parser):
    def __init__(self):
        self.url = 'https://www.uhovezihopupku.cz/menu/'
        super(Pupek, self).__init__(self.url)

        self.daily_menu_tag_data = ['table', {'class': 'menu_den'}]
        self.menu_item_tag_data = 'tr'
        self.meal_tag_data = ['td', {'class': 'menu_jidlo_text'}]
        self.meal_price_tag_data = ['td', {'class': 'menu_jidlo_cena'}]

    def process(self):
        week_menu = self.get_all_elements(self.html_object, self.daily_menu_tag_data)

        if len(week_menu) > 0:
            self.process_week_menu(week_menu)

        self.print()

    def process_week_menu(self, week_menu):
        for daily_menu in week_menu:
            menu_item_elements = self.get_all_elements(daily_menu, self.menu_item_tag_data)

            if len(menu_item_elements) > 0:
                self.process_menu_items(menu_item_elements)

    def process_menu_items(self, menu_items):
        daily_menu = DailyMenu()

        date = menu_items[0].get_text().strip()
        daily_menu.set_date(date)

        for item in menu_items[1:]:
            meal = Meal()

            meal_element = self.get_element(item, self.meal_tag_data)
            price_element = self.get_element(item, self.meal_price_tag_data)

            if meal_element is not None:
                meal.set_text(meal_element.get_text().strip())

            if price_element is not None:
                meal.set_price(price_element.get_text().strip())

            if 'menu_jidlo_polevka' in meal_element['class']:
                daily_menu.add_soup(meal)
            else:
                daily_menu.add_meal(meal)

        self.weekly_menus.append(daily_menu)


Pupek().process()