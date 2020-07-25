class DailyMenu:
    def __init__(self):
        self.date = None
        self.soups = []
        self.meals = []

    def set_date(self, date):
        self.date = date

    def add_soup(self, soup):
        self.soups.append(soup)

    def add_meal(self, meal):
        self.meals.append(meal)