#write functions here, don't add input('') statements here!

def get_miles_per_hour(kilometers, minutes):
    if kilometers < 0 or minutes <= 0:
        return "Invalid Arguments"
    else:
        miles_per_hour = (kilometers / minutes) * 60 * .621371
        return miles_per_hour