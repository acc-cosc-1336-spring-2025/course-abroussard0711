#Homework 3


# define the for function to determine the factorial of the num variable
def get_factorial(num):
    
    result = 1
    
    for i in range(1, num + 1):
        result *= i
    
    return result


# define while loop that will sum all odd numbers up to the num variable value
def sum_odd_numbers(num):
    
    total = 0
    i = 1

    while (i <= num):
        if i % 2 != 0:
            total += i
        
        i += 1
    
    return total



# validates the integer input of the get_factorial input is within the parameters
def get_valid_number_for_factorial():
    while True:
        try:
            num = int(input('Enter a number between 0 and 10: '))
            if 0 < num < 10:
                return num
            else:
                print('Number must be greater than 0 and less than 10. Please try again.')
        except ValueError:
            print('Invalid input. Please try again.')


# validates the integer input of sum_odd_numbers are within the parameters
def get_valid_number_for_sum():
    while True:
        try:
            num = int(input('Enter a number between 0 and 100: '))
            if 0 < num < 100:
                return num
            else:
                print('Number must be greater than 0 and less than 100. Please try again.')
        except ValueError:
            print('Invalid input. Please try again.')


# prompts the user if they want to exit. If 'y', the program will exit. If 'n', the function returns and will be shown again.
def exiting_func():
    exit_choice = input ('Do you want to exit? (Y/N): ')
    if exit_choice in ('y', 'yes'):
        print ('Exiting... ')
        exit()
    elif exit_choice in ('n', 'no'):
        print ('Continuing program... ')
        return
    else:
        print ('Invalid input. Please answer with "y" or "n".')


# defines and displays the user input menu
def display_menu():
    print ('Homework 3 Menu')
    print ('1-Factorial')
    print ('2-Sum odd numbers')
    print ('3-Exit')


# defines and runs the user menu and prompt for inputs
def run_menu():
    user_option = '0'

    while (user_option != '3'):
        display_menu()

        user_option = input ('Enter a menu option 1, 2, or 3: ')
        handle_menu (user_option)



# defines the input menu and its actionable items that reference the get_factorial and sum_odd_numbers functions
def handle_menu(user_option):

    if (user_option == '1'):
        number = get_valid_number_for_factorial()
        result = get_factorial (number)
        print ('Factorial = ', result)    
      
    elif (user_option == '2'):
        number = get_valid_number_for_sum()
        result = sum_odd_numbers (number)
        print ('Sum of odds = ', result)

    elif (user_option == '3'):
        print ('Exiting... ')

    else: 
        print ('Invalid menu option')

    exiting_func()



