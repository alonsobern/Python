import pandas as pd

def convert_price(dataframe,column):
    for index, value in enumerate(dataframe[column]):
        if "$" in str(value):
            dataframe.loc[index,column] = str(value).replace("$","")
    
    for index, value in enumerate(dataframe[column]):
        if "," in str(value):
            dataframe.loc[index,column] = str(value).replace(",","")

    dataframe[column] = pd.to_numeric(dataframe[column])

    return dataframe[column]



def convert_rate(dataframe,column):
    for index, value in enumerate(dataframe[column]):
        if "%" in str(value):
            dataframe.loc[index,column] = str(value).replace("%","")

    dataframe[column] = pd.to_numeric(dataframe[column])
    dataframe[column] = dataframe[column]/100

    return dataframe[column]