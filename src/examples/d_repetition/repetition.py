def test_config():
    return True

def test_config():
    return True

def use_a_while_loop(num):
    
    counter = 0
    
    while (counter < num): #boolean expression while true loops if false stops looping
        print(counter, counter < num, 'Hello world.')
        counter = counter + 1 #statement that makes the boolean expression false

        if(counter == 3):
            print(counter, counter < num, '')

# with a defined number the function will calculate the sum of squares (1*1 + 2*2 + 3*3 + n*n)

def get_sum_of_squares(num1):

    sum = 0

    while (num1 > 0):
        sum = sum + num1 * num1
        num1 = num1 - 1 # will make the defined number less than zero to produce a False statement

    return sum

def display_menu():
    print ('1-Use a while loop')
    print ('2-Sum of squares')
    print ('3-Exit')

def run_menu():
    user_option = "0"

    while (user_option != '3'):
        display_menu()

        user_option = input ("Enter a menu option (1,2,3): ")
        handle_menu (user_option)

def handle_menu(user_option):
    if (user_option == '1'):
        num = input ("Enter a number: ")
        result = use_a_while_loop(int(num))

    elif (user_option == '2'):
        num = input ("Enter a number: ")
        result = get_sum_of_squares (int(num))
        print ("Get sum of squares: ", result)

    elif (user_option == '3'):
        print ('Exiting.... ')

    else: 
        print ("Invalid menu option")
        

# example code from class on Wed 02/19/25

def use_a_for_range_loop(num):
    for val in range(0, 3):
        print(val, 'hello')


def get_sum_of_squares_for(num1):
    sum = 0

    for n in range(0, num1):
        sum = sum + (n + 1) * (n + 1)

    return sum

def nested_while_loop(num):
    i = 0

    while (i < num):
        j = 0
        print (i , "Waiting for inner while loop... ")

        while (j < num):
            j += 1
            print (j , "\tInner while loop running... ")

            i += 1

def for_nested_loop(num):

    for i in range (0, num):
        print('Waiting for inner loop... ')

        for j in range (0, num):
            print ('\t Inner loop running... ')


def multiplication_table_while(rows,cols):
    r = 0

    while (r < rows):
        c = 0

        while (c < cols):
            product = (r + 1) * (c +1)
            print (str(product).rjust(3, " "), end = " ")

            c += 1 # to complete inner loop

        r += 1 # to complete outer loop
        print (" ")


def multiplication_table_for(rows, cols):

    for r in range(0, rows):
        for c in range(0, cols):
            product = (r + 1) * (c + 1)
            print(str(product).rjust(3, " "), end = " ")

        print(" ")