# functions to gather user inputs and pass through min and max functions


# function to determine lowest value in user list using for loop
def get_lowest_list_value (numbers):
    if not numbers: 
        return ()               # return none if the list is empty
    
    lowest = numbers [0]        # assuming the first element of the list is the lowest value

    for num in numbers [1:]:    # for loop to compare and reassign the rest of the list
        if num < lowest:
            lowest = num        # update lowest value if smaller value is found

    return lowest


# function to determine highest value in user list using for loop
def get_highest_list_value (numbers):
    if not numbers: 
        return ()               # return none if the list is empty
    
    highest = numbers [0]       # assuming the first element of the list is the highest value

    for num in numbers [1:]:    # for loop to compare and reassign the rest of the list
        if num > highest:
            highest = num       # update highest value if larger value is found

    return highest


# function to obtain user input values in list
def get_number_list ():

    number_list = []            # create empty list to store user inputs

    again = 'y'                 # define variable in while loop

    first_loop = 0              # define variable in for loop

    for n in range (0,2):       # prompts user for the first two values in the list
        number1 = int (input ('Enter a value: '))

        number_list.append(number1)

        first_loop += 1

    while again == 'y':                 # prompts user for a third and optional additional values
        number2 = int (input ('Enter a value: '))
        
        number_list.append(number2)     # appends the user list with additional values         
        
        print ('Do you want to add another number?')        # prompts user for optional values
        
        again = input('y = yes, anything else = no: ')      # user inputs
        
        print ()
        print ('Here are the numbers you entered.')         

    print (number_list)                 # displays the user inputs

    return number_list                  # returns the list elements of the user inputs


# defines and displays the user input menu
def display_menu ():
    print ('Choose a menu option below:')
    print ('1 - Show the list low /high values')
    print ('2 - Exit')
    print ('')


# defines and runs the user menu and prompt for inputs
def run_menu ():
    while True:
        display_menu ()

        user_option = input ('Enter a menu option 1 or 2: ')        # prompts user to choose between two options
        handle_menu (user_option)

        if user_option == '2':                                      # confirms user input to exit the program
            confirm_exit = input ('Are you sure you want to exit? (y/n)')

            if confirm_exit == 'y':                                 # exits program
                print ('Exiting program... ')
                break
            else:                                                   # continues program
                print ('Continuing program... \n')
                

# defines the input menu and its actionable items that reference the get_factorial and sum_odd_numbers functions
def handle_menu(user_option):

    if (user_option == '1'):                # program runs for option choice 1
        number = get_number_list()          # calls elements of user defined list
        
        result1 = get_lowest_list_value (number)        # passes user defined list through lowest value function
        result2 = get_highest_list_value (number)       # passes user defined list through highest value function
        
        print ('The lowest number is ', result1)        # displays lowest value
        print ('The highest number is ', result2)       # displays highest value
      
    elif (user_option == '2'):              # program exits for option choice 2
        print ('Exit selected. ')
    
    else: 
        print ('Invalid menu option')


    