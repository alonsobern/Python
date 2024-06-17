import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as cx
import seaborn as sns

class Menuview:
    def display_items(self, title, items):
        print(f"{title}:")
        for item in items:
            print(f"-{item}")
    
class DataView:
    
    def display_data_map_prices(self, title, data, x, y):
        
        print(f"{title}")
        print("Loading...")

        # Using geopandas to convert long and lat to geometry points
        df_geo = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.longitude, data.latitude), crs='EPSG:4326')

        sns.set(style="darkgrid", palette="deep")
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9,9))
        
        # Plotting the barplot
        sns.barplot(data=data, x=x, y=y, ax=axes[0], capsize=0.20, legend=True, hue=x)

        # Grouping by Neighbourhoods
        x_dfgeo = df_geo.dissolve(by=x, aggfunc="mean")

        # Plotting the map classifying by quantiles
        ax = x_dfgeo.to_crs('EPSG:3857').plot(cmap='jet',
                                             column=y,
                                             scheme="quantiles",
                                             k=4,
                                             alpha=0.9,
                                             markersize=8,
                                             ax=axes[1],
                                             legend=True,
                                             legend_kwds={'title': "Ranges Prices ($)", 'loc':"upper left", 'fancybox':True, 'shadow':True})
        

        # Titles
        axes[0].set_title("Barplot based on Prices (avg) by Neighbourhood", fontsize=15)
        axes[0].set_ylabel("Price (Avg)", fontsize=12)
        axes[0].set_xlabel("Neighbourhoods", fontsize=12)
        axes[0].legend(fancybox=True, shadow=True)
        axes[1].set_title("Geospatial Information based on Ranges Prices", fontsize=15)

        # add the annotation for the barplot
        for i in range(0,4):
            axes[0].bar_label(axes[0].containers[i], fmt='\n\n\n\nMean:\n%.2f', label_type='center', fontsize=10)

        cx.add_basemap(ax, zoom=12)
        cx.add_basemap(ax, source=cx.providers.CartoDB.PositronOnlyLabels, zoom=10)
        plt.tight_layout()
        plt.show()
    
    def display_data_map_rating(self, title, data, x, y, query=None):
        print(f"{title}")
        print("Loading...")

        sns.set(style="darkgrid", palette="deep")
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,12))

        # Querying
        if query is None:
            dataDFQuery = data.copy()
        else:
            dataDFQuery = data.query(query)

        # Plotting the barplot
        sns.barplot(data=dataDFQuery, x=x, y=y, ax=axes[0], hue='neighbourhood_cleansed', capsize=0.20)

        # Transforming the data in geometry data
        df_geo = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.longitude, data.latitude), crs='EPSG:4326')
        
        # Querying
        if query is None:
            df_geoQuery = df_geo.copy()
        else:
            df_geoQuery = df_geo.query(query)

        # Classifying by the nomimal data
        x_dfgeo = df_geoQuery.dissolve(by=['neighbourhood_cleansed','room_type'], aggfunc="mean")

        # Plotting the map classifying by quantiles
        ax = x_dfgeo.to_crs('EPSG:3857').plot(cmap='jet',
                                             column=x,
                                             scheme="quantiles",
                                             k=4,
                                             alpha=0.9,
                                             markersize=10,
                                             ax=axes[1],
                                             legend=True,
                                             legend_kwds={'title': "Review Rating", 'loc':"lower left", 'fancybox':True, 'shadow':True})

        # Titles
        axes[0].set_xlabel("Review Rating Score", fontsize=12)
        axes[0].set_ylabel("Room type", fontsize=12)
        axes[0].legend(ncol=2, bbox_to_anchor=(0.5, 1.1), loc='upper center', frameon=True, draggable=True, fancybox=True, shadow=True)
        axes[0].set_title("Barplot based on Room type by Neighbourhood")
        axes[1].set_title("Geospatial Information based on Review Rating Score", fontsize=12)

        # Annotation for the bar plot
        if query == "room_type == 'Shared room'":
            for i in range(0,3):
                axes[0].bar_label(axes[0].containers[i], fmt='Rating (avg):\n%.2f', label_type='center', fontsize=10)
        else:
            for i in range(0,4):
                axes[0].bar_label(axes[0].containers[i], fmt='Rating (avg):\n%.2f', label_type='center', fontsize=10)

        cx.add_basemap(ax, zoom=11)
        plt.tight_layout()
        plt.show()