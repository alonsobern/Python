import pandas as pd

class MenuModel:
    def __init__(self) -> None:
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items
    
class DataModel:
    def __init__(self) -> None:
        self.data = pd.read_csv("Data/airbnb_listings.csv")

    def get_mean(self, variable):
        return round(self.data[variable].mean(),3)
    
    def get_data_map(self,variable):
        features = variable+['latitude','longitude']
        map_kpi = self.data.loc[:,features]
        if 'price' in features:
            map_kpi['price'] = map_kpi['price'].replace('[$,]','',regex=True).astype(float)
        map_kpi.dropna(inplace=True)
        map_kpi.sort_values(by=variable, ascending=False, inplace=True)
        return map_kpi
