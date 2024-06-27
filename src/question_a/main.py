#add import
#import get_assessment_value, get_tax_assessed
from question_a import get_assessment_value, get_tax_assessed

def get_value_and_tax():
    quit_condition = False

    while not quit_condition:
        land_value = input("Welcome! Please enter the value of the land you are interested in getting the assessment value and tax assessed for (or enter 'q' to quit): ")
        if land_value.lower() == "q":
            quit_condition = True
        else:
            if land_value.isdigit():
                land_value = int(land_value)
                assessment = get_assessment_value(land_value)
                print("Assessment Value: $", assessment)
                tax = get_tax_assessed(assessment)
                print("Tax Assessed: $", tax)
            else:
                print("Please enter a valid integer or 'q' to quit: ")
get_value_and_tax()