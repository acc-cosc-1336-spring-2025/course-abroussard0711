#

from class_a import Die


def main():

    while True:
        print ('User Menu:')
        print ('1 - Roll Die')
        print ('2 - Exit Program')

        choice = input('What would you like to do? Enter action 1 or 2: ')

        if choice == '1':
            my_die = Die()
            
            while True:
                input('Press Enter to roll the die...')
                my_die.roll()
                print(my_die)  # uses the __str__ method to show the rolled value
                
                roll_again = input('Do you want to roll again? (y/n): ').strip().lower()
        
                if choice != 'y':
                    print('Returning to the main menu...')
                    break
        
        elif choice == '2':
            print ('Exiting program...')
            break

        else:
            print ('Invalid input')

main ()