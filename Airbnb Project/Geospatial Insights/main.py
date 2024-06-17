import os
import time
from Model.model import MenuModel, DataModel
from View.view import Menuview, DataView
from Controller.controller import MenuController, DataController

menu_model = MenuModel()
menu_view = Menuview()
menu_controller = MenuController(menu_model,menu_view)
menu_controller.add_item("1. Based on price")
menu_controller.add_item("2. Based on review rating score")
menu_controller.add_item("3. Exit")
menu_controller.display_view(title="Geospatial Interface Airbnb:")


flag = True
while flag:

    try:
        os.system('cls')
        menu_controller.display_view(title="Geospatial Interface Airbnb:")

        menu_input = int(input("Enter your option: "))

        if menu_input == 1:
            os.system('cls')
            based_on_priceModel = DataModel()
            based_on_priceView = DataView()
            based_on_priceController = DataController(based_on_priceModel,based_on_priceView)
            based_on_priceController.display_map_prices(title="Statistics based on price", 
                                                        variables=['neighbourhood_cleansed','price'], 
                                                        x='neighbourhood_cleansed', 
                                                        y='price')
        elif menu_input == 2:
            flag_rating = True
            os.system('cls')
            menu_ratingModel = MenuModel()
            menu_ratingView = Menuview()
            menu_ratingController = MenuController(menu_ratingModel, menu_ratingView)

            based_on_ratingModel = DataModel()
            based_on_ratingView = DataView()
            based_on_ratingController = DataController(based_on_ratingModel,based_on_ratingView)
            based_on_ratingController.display_map_rating(title="Statistics based on review rating score",
                                                        variables=['neighbourhood_cleansed','room_type','price','review_scores_rating'],
                                                        y='room_type',
                                                        x='review_scores_rating',
                                                        query=None)
            
            menu_ratingController.add_item("1. Query by Shared room")
            menu_ratingController.add_item("2. Query by Private room")
            menu_ratingController.add_item("3. Query by Entire home/apt")
            menu_ratingController.add_item("4. Query by Hotel room")
            menu_ratingController.add_item("5. Back to the menu")
            menu_ratingController.display_view(title="Rating Review Scores Menu")

            while flag_rating:

                try:
                    os.system('cls')
                    menu_ratingController.display_view(title="Rating Review Scores Menu")

                    menu_rating = int(input("Enter your option: "))

                    if menu_rating == 1:
                        os.system('cls')
                        based_on_ratingController.display_map_rating(title="Statistics based on review rating score", 
                                                                    variables=['neighbourhood_cleansed','room_type','price','review_scores_rating'], 
                                                                    y='room_type', 
                                                                    x='review_scores_rating',
                                                                    query="room_type == 'Shared room'")
                    elif menu_rating == 2:
                        os.system('cls')
                        based_on_ratingController.display_map_rating(title="Statistics based on review rating score", 
                                                                    variables=['neighbourhood_cleansed','room_type','price','review_scores_rating'], 
                                                                    y='room_type', 
                                                                    x='review_scores_rating',
                                                                    query="room_type == 'Private room'")
                    elif menu_rating == 3:
                        os.system('cls')
                        based_on_ratingController.display_map_rating(title="Statistics based on review rating score", 
                                                                    variables=['neighbourhood_cleansed','room_type','price','review_scores_rating'], 
                                                                    y='room_type', 
                                                                    x='review_scores_rating',
                                                                    query="room_type == 'Entire home/apt'")
                    elif menu_rating == 4:
                        os.system('cls')
                        based_on_ratingController.display_map_rating(title="Statistics based on review rating score", 
                                                                    variables=['neighbourhood_cleansed','room_type','price','review_scores_rating'], 
                                                                    y='room_type', 
                                                                    x='review_scores_rating',
                                                                    query="room_type == 'Hotel room'")
                    elif menu_rating == 5:
                        flag_rating = False
                    else:
                        os.system('cls')
                        print("You need to choose a correct option to proceed, please pick an option from the menu.")
                        print("\nYou will be redirected to the main menu automatically.")
                        time.sleep(3)
                        
                except ValueError:
                    os.system('cls')
                    print("Oops!  That was no valid number.  Try again...")
                    print("\nYou will be redirected to the main menu automatically.")
                    time.sleep(3)

        elif menu_input == 3:
            exit()
        else:
            os.system('cls')
            print("You need to choose a correct option to proceed, please pick an option from the menu.")
            print("\nYou will be redirected to the main menu automatically.")
            time.sleep(3)
            
    except ValueError:
        os.system('cls')
        print("Oops!  That was no valid number.  Try again...")
        print("\nYou will be redirected to the main menu automatically.")
        time.sleep(3)