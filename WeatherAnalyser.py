import random

def getValues(x):
    values = list()
    for i in range(30):
        values.append(random.randint(0,x))
    return values

def getLowestValue(vector):
    lowestValue = vector[0]
    for i in range(len(daily_temperatures)):
        j = i+1 if i<len(vector)-1 else i
        if vector[j] < lowestValue:
            lowestValue = vector[j]
    return lowestValue

def getHighestValue(vector):
    highestValue = vector[0]
    for i in range(len(vector)):
        j = i+1 if i<len(vector)-1 else i
        if vector[j] > highestValue:
            highestValue = vector[j]
    return highestValue

def getDays(vector, x, flag):
    days = list()
    for day, value in enumerate(vector):
        if value > x and flag == "above":
            days.append(day+1)
        elif value < x and flag == "below":
            days.append(day+1)
        elif x == value and flag == "equal":
            days.append(day+1)
    return days

def getDaysWeather(temperatures, rainfalls, flag):
    c = 0
    for temperature, rainfall in zip(temperatures, rainfalls):
        if temperature < 10 and rainfall > 3 and flag == "badweather":
            c += 1
        elif 18 >= temperature >= 10 and 5 >= rainfall >= 1 and flag == "averageweather":
            c += 1
        elif temperature > 18 and rainfall < 2 and flag == "goodweather":
            c += 1
    return c

def getDaysTemperatureIncreased(vector):
    days = list()
    for day, value in enumerate(vector):
        j = day + 1 if day < len(vector)-1 else day
        if vector[j] > value:
            days.append(j+1)
    return days

daily_temperatures = getValues(35)
daily_rainfall = getValues(10)
print("\nWeather Analyser\n")
print("Temperatures:", daily_temperatures)
print("Rainfalls:   ", daily_rainfall)

print("\n")
print("Lowest Temperature:", getLowestValue(daily_temperatures))
print("Highest Temperature:", getHighestValue(daily_temperatures))
print("Lowest Rainfall:", getLowestValue(daily_rainfall))
print("Highest Rainfall:", getHighestValue(daily_rainfall))

print("\n")
print("Lowest Temperature day(s):", getDays(daily_temperatures, getLowestValue(daily_temperatures), "equal"))
print("Highest Temperature day(s):", getDays(daily_temperatures, getHighestValue(daily_temperatures), "equal"))
print("Day(s) where the temperature rises above 20C:", getDays(daily_temperatures, 20, "above"))
print("Day(s) where the temperature drops below 10C:", getDays(daily_temperatures, 10, "below"))

print("\n")
print("Bad Weather day(s):", getDaysWeather(daily_temperatures, daily_rainfall, "badweather"))
print("Average Weather day(s):", getDaysWeather(daily_temperatures, daily_rainfall, "averageweather"))
print("Good Weather day(s):", getDaysWeather(daily_temperatures, daily_rainfall, "goodweather"))
print("Day(s) of temperature increased from the day before:", getDaysTemperatureIncreased(daily_temperatures))