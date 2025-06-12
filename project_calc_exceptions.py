# Project: Calculator with Exception Handling
# Mandy Lubinski

import logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(levelname)s:%(message)s')

def menu():
    # Input for user to see useful information to run the program
    while True:
        print("\nWelcome to the Error-Free Calculator!")
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("> ")

        # Addition
        if choice == "1":
            try:
                n1 = float(input("Enter the first number: "))
                n2 = float(input("Enter the second number: "))
                result = n1 + n2  
            except ValueError as e:
                print("Invalid input! Please enter a valid number.")
                logging.error(f"ValueError occurred: {e}")
            else:
                print(f"The result is {result}")
            finally:
                print("Thanks for using the Error-Free Calculator today!")
        
        # Subtraction
        elif choice == "2":
            try:
                n1 = float(input("Enter the first number: "))
                n2 = float(input("Enter the second number: "))
                result = n1 - n2  
            except ValueError as e:
                print("Invalid input! Please enter a valid number.")
                logging.error(f"ValueError occurred: {e}")
            else:
                print(f"The result is {result}")
            finally:
                print("Thanks for using the Error-Free Calculator today!")
        
        # Multiplication
        elif choice == "3":
            try:
                n1 = float(input("Enter the first number: "))
                n2 = float(input("Enter the second number: "))
                result = n1 * n2  
            except ValueError as e:
                print("Invalid input! Please enter a valid number.")
                logging.error(f"ValueError occurred: {e}")
            else:
                print(f"The result is {result}")
            finally:
                print("Thanks for using the Error-Free Calculator today!")
        
        # Division 
        elif choice == "4":
            try:
                n1 = float(input("Enter the first number: "))
                n2 = float(input("Enter the second number: "))
                result = n1 / n2  
            except ValueError as e:
                print("Invalid input! Please enter a valid number.")
                logging.error(f"ValueError occurred: {e}")
            except ZeroDivisionError as e:
                print("Oops! Division by zero is not allowed.")
                logging.error(f"ZeroDivisionError occurred: {e}")
            else:
                print(f"The result is {result}")
            finally:
                print("Thanks for using the Error-Free Calculator today!")
        
        # Quit 
        elif choice == "5":
            print("Goodbye!")
            break
            
        # To ensure that the user inputs a valid number for the program to run
        else:
            print("Invalid option. Please enter 1, 2, 3, 4, or 5.")

menu()