#add import
from c_functions import get_person_category

def main():

    while True:
        
        age = int(input("Enter age: "))
        category = get_person_category(age)
        
        if category != "Invalid":
            print(f"A person of {age} year(s) old is a(n) {category}")
            break
        else:
            print(f"{age} is an invalid age")

if __name__ == "__main__":
    main()