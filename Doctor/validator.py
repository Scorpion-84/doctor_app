import re


def ills_validator(ill):
    errors = []
    if not (type(ill[0]) == int and ill[0]>0):
        errors.append('Person ID must be an integer > 0')

    if not (type(ill[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", ill[1])):
        errors.append('Person Name is Invalid')


    if not (type(ill[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", ill[2])):
        errors.append('Person Family is Invalid')

    if not (type(ill[3]) == int and ill[3]>0):
        errors.append('Person Account Amount must be an integer > 0')

    return errors