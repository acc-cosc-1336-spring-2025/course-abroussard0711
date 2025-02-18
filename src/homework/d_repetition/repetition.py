#

def test_config():
    return True

def use_a_while_loop(num):
    
    counter = 0
    
    while (counter < num): #boolean expression while true loops if false stops looping
        print(counter, counter < num, 'Hello world.')
        counter = counter + 1 #statement that makes the boolean expression false

        if(counter == 3):
            print(counter, counter < num, '')
    