#

# function to determine the p distance between two lists
def get_p_distance (list1, list2):

    differences = 0                     # defines the variable 'differences' to use in the for loop
    length = len(list1)                 # defines the variable 'length' to hold the length of list1

    for s1, s2 in zip(list1, list2):    # for loop to check that the DNA sequences are of equal length
        if s1 != s2:
            differences += 1

    return differences / length         # return the proportion of the differences of the elements p distance


# function to create the p distance matrix
def get_p_distance_matrix (lists):

    string_length = len(lists)          # defines the variable 'string_length' to hold the length of lists
    p_distance_matrix = []              # creates an empty list to use in the for loop to compare the DNA sequence elements

    for i in range(string_length):      # for loop to compare the corresponding symbols in the DNA sequences
        row = []                        # creates an empty list to use in the comparison 
        for j in range(string_length):
            dist = get_p_distance(lists[i], lists[j])
            row.append(round(dist, 5))  # appends the sequence rows with the differences
        p_distance_matrix.append(row)

    return p_distance_matrix            # returns the variance list



# function to obtain user input values in list
def get_DNA_strings ():
    
    try:
        n = int(input("How many DNA sequences will you enter? (max 6): "))
        
        if n < 2 or n > 6:          # confirms the user inputs are within the parameters
            print("Please enter between 2 and 6 sequences.")
            return None
            
        sequences = []                                      # create empty list to store user inputs
        
        for i in range(n):
            seq = input(f"Enter sequence {i + 1}: ").strip().upper()        # prompts user for a DNA strings and displays the next sequence number
            sequences.append(seq)

        length_set = {len(seq) for seq in sequences}        # checks all sequences are of equal length
        
        if len(length_set) != 1:                            # warning message that not all strings are of equal length
            print("Error: All sequences must be of equal length.")
            return None

        return sequences                                    # returns the user inputs
            
        
    except ValueError:                                      # warning message that user inputs are invalid
        print("Invalid input. Please enter numeric values where required.")
    

# defines and displays the user input menu
def display_menu ():
    print ('Choose a menu option below:')
    print ('1 - Get p distance matrix')
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

    if (user_option == '1'):                              # program runs for option choice 1
        
        strings = get_DNA_strings()                       # calls elements of user defined list
        
        result = get_p_distance_matrix (strings)          # passes user defined strings through matrix function

        print ('The p distance matrix is ', result)       # displays p distance matrix
      
    elif (user_option == '2'):                            # program exits for option choice 2
        print ('Exit selected. ')
    
    else:                                                 # warning message that user inputs are invalid
        print ('Invalid menu option')
