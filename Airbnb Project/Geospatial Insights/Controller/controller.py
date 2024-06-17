from Model.model import MenuModel, DataModel
from View.view import Menuview, DataView

class MenuController:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def add_item(self, item):
        self.model.add_items(item)

    def display_view(self, title):
        items = self.model.get_items()
        self.view.display_items(title, items)

class DataController:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def display_value(self, title, variables, orderby, groupby):
        data = self.model.get_data_map(variables)
        self.view.display_data_values(title, data, orderby, groupby)
    
    def display_map_prices(self, title, variables, x, y):
        data = self.model.get_data_map(variables)
        self.view.display_data_map_prices(title, data, x, y)
    
    def display_map_rating(self, title, variables, x, y, query):
        data = self.model.get_data_map(variables)
        self.view.display_data_map_rating(title, data, x, y, query)
        