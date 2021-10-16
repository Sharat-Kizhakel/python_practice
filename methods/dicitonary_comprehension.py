# dictionary comprehension=create dictionaries using an expression
# can replace for loops and certain lambda functions
# dictionary={key:expression for (key,value) in iterable}
# note:expression can be another function
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

cities_in_C = {key: round((value - 32) * (5 / 9))
               for (key, value) in cities_in_F.items()}

print(cities_in_C)

weather = {'New York': "cloudy", 'New jersey': "rainy", 'Louisiana': "sunny",
           'Southampton': "cloudy", 'Los Angeles': "rainy", 'California': "cloudy"}

cloudy_weather = {key: value for (
    key, value) in weather.items() if value == "cloudy"}
print(cloudy_weather)
dict_desc = {key: ("WARM" if value <= 30 else "COLD")
             for (key, value) in cities_in_F.items()}
print(dict_desc)

# note:expression can be another function


def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"


dict_expr = {key: check_temp(value) for (key, value) in cities_in_F.items()}
print(dict_expr)
