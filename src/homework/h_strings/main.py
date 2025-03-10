# define the main function to call the get_hamming_distance function and the get_dna_complement function

import strings

def main():
    result = run_menu()
    print = result

# defines and displays the user input menu
def display_menu():
    print ('Homework 5 Menu')
    print ('1-Hamming Distance')
    print ('2-DNA Complement')
    print ('3-Exit')


# defines and runs the user menu and prompt for inputs
def run_menu():
    user_option = '0'

    while (user_option != '3'):
        display_menu()

        user_option = input ('Enter a menu option 1, 2, or 3: ')
        handle_menu (user_option)


# defines the input menu and its actionable items that reference the get_hamming_distance and get_dna_complement functions
def handle_menu(user_option):

    if (user_option == '1'):
        s = input ("Enter a DNA sequence: ")
        t = input ("Enter another DNA sequence: ")
        result = strings.get_hamming_distance(s,t)
        print ('The Hamming distance is = ', result)    
      
    elif (user_option == '2'):
        seq = input ("Enter a DNA sequence: ")
        result = strings.get_dna_complement(seq)
        print ("The DNA Complement is: ", result)

    elif (user_option == '3'):
        print ('Exiting... ')

    else: 
        print ('Invalid menu option')

main ()
