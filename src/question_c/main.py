#add import
from question_c import get_miles_per_hour


def mph_converter():
    kilometers = int(input("Welcome! To get Miles Per Hour please enter Kilometers first: "))
    minutes = int(input("Then Minutes: "))
    miles_per_hour = get_miles_per_hour(kilometers, minutes)

    if miles_per_hour == "Invalid Arguments":
        print(miles_per_hour)
    else:
        print(str(miles_per_hour) + " miles per hour (mph)")
mph_converter()