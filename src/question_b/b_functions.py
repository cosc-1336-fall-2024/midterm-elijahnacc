#write functions here, don't add input('') statements here!

def get_bonus_pay_amount(sales):

    bonus = 0

    if sales < 0 or sales >= 2000:
        bonus = "Invalid"
    elif sales >= 1500:
        percent = 0.08
    elif sales >= 1000:
        percent = 0.07
    elif sales >= 500:
        percent = 0.06
    elif sales >= 0:
        percent = 0.05

    if bonus != "Invalid":
        bonus = sales * percent

    return bonus