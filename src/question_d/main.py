#add import
#import get_assessment_value, get_tax_assessed
from question_d import reverse_string

def get_string_to_reverse():
    quit_condition = False

    while not quit_condition:
        string_to_reverse = input("Welcome! Please enter the phrase you would like reversed (or enter 'q' to quit): ")
        if string_to_reverse.lower() == "q":
            quit_condition = True
        else:
            output = reverse_string(string_to_reverse)
            print(output)
get_string_to_reverse()