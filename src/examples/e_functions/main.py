#main program

import value_return_functions

def main ():

    num = 3
    result = value_return_functions.echo_variable(num)
    print (result)

    for i in range(0,20):
        results = value_return_functions.get_random_number(1,100)
        print (results)

main ()

