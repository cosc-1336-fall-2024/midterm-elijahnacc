#write functions here, don't add input('') statements here!

def get_person_category(age):

    if age < 0 or age > 125:
        category = "Invalid"
    elif age >= 20:
        category = "Adult"
    elif age >= 13:
        category = "Teenager"
    elif age > 1:
        category = "Child"
    elif age <= 1:
        category = "Infant"
    
    return category