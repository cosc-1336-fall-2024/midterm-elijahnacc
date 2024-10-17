#add import
from b_functions import get_bonus_pay_amount

def main():
    
    while True:
        
        sales = int(input("Enter sales amount: "))
        bonus = get_bonus_pay_amount(sales)

        if bonus == "Invalid":
            print("Invalid Arguments")
        else:
            bonus = str(round(bonus, 2))
            print(f"The bonus pay for {sales} sales is ${bonus}")
            break

    exit()


if __name__ == '__main__':
    main()