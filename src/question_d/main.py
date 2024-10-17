#add import
from d_functions import get_assessment_value, get_tax_assessed

def main():

    valid_y = {"y", "Y"}
    valid_n = {"n", "N"}


    while True:

        cont = ""

        property_value = int(input("Please enter property value: "))
        assessment_value = get_assessment_value(property_value)
        property_tax = get_tax_assessed(assessment_value)

        print(f"The property is assessed at {assessment_value}, and will be taxed at {property_tax}")

        while cont not in valid_y:

            cont = input("Would you like to assess another property? y/n: ")

            if cont in valid_n:
                exit()
            elif cont in valid_y:
                break
            else:
                print("Invalid selection")
            
if __name__ == "__main__":
    main()