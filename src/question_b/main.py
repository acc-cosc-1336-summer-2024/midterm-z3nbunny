#add import

from question_b import get_fahrenheit

def conversion_table():
    print("Celsius  Fahrenheit")
    print("___________________")
    for celsius in range(21):
        fahrenheit = get_fahrenheit(celsius)
        print(str(celsius) + "           " + str(fahrenheit))
conversion_table()