#write functions here, don't add input('') statements here!

def reverse_string(string1):
    reversed_string = ""
    i = len(string1) - 1
    while i >= 0:
        reversed_string += string1[i]
        i -= 1
    return reversed_string