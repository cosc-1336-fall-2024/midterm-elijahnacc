#add import
from a_functions import reverse_string

def main():

    string = ""
    
    while string != "3":
        string = str(input("Enter String or press 3 to Exit: "))

        if string == "3":
            break

        print(reverse_string(string))

    exit()

if __name__ == '__main__':
    main()