#to execute the get_options_ratio and get_faculty_rating functions

import decisions

#defining the main function

def main(): 
    # get the variable value of options as a float
    options = float (input ('What is the option value? '))

    # get the variable value of total as a float
    total = float (input ('What is the total value? '))

    #creates the result variable with user inputs for options and total    
    result = decisions.get_options_ratio(options, total) 
    
    #prints the result
    print(result)   

#runs the code block beginning on line 7
main()  