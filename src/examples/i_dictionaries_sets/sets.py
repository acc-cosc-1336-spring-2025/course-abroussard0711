# Class example - Survey Analysis (App): 

# Requirements
# 1) Display Questions / Options
# 2) Capture/ Save Responses (options)
# 3) Tabulate Responses
#   a. Course
#   b. Determine Rating (pass, good, excellent)
# 4) Validate response
# 5) Survey menu

# Details:
# Dictionary - questions
# Dictionary - options
# Dictionary - 


#Create dictionaries

survey_questions = \
{
    '2.1': 'Question 1',
    '2.2': 'Question 2',
    '2.3': 'Question 3',
    '2.4': 'Question 4',
    '2.5': 'Question 5'

}

survey_options = \
{
    '1' : 'Never',
    '2' : 'Sometimes',
    '3' : 'More',
    '4' : 'Always',
    '5' : 'n/a'

}

# list of lists
survey_response_list = [] #survey_id, question_id, response

survey_response_results = {}

survey_response_results_total = {'2.1': 0, '2.2': 0, '2.3': 0, '2.4': 0, '2.5': 0}


def display_survey_questions ():

    survey_id = 1

    for question_id, question in survey_questions.items ():
        print (question_id, question)

        for option, value in survey_options.items ():
            print (option, value)

        response = int (input ('Enter response: '))
        capture_survey_response (survey_id, question_id, response)
        survey_id += 1

def capture_survey_response (survey_id, question_id, response):

    survey_response_list.append ([survey_id, question_id, response])
    print (survey_response_list)


def tabulate_survey_response_results ():

    cnt = 0

    for response in survey_response_list:
        print (response)

        survey_response_results_total [response[1]] += response[2]

        if '2.5' == response[1]:
            cnt += 1

    print (survey_response_results_total)


def display_menu ():
    print ('1 - Enter survey responses')
    print ('2 - Get Survey Results')
    print ('3 - Exit')

def run_menu ():
    
    option = 0

    while option != 3:
        display_menu ();
        option = int (input('Enter option: '))
        handle_menu_option (option)


def handle_menu_option (option):

    if (option == 1):
        print ('display survey question')
        display_survey_questions ()
    elif (option == 2):
        print ('survey results')
        tabulate_survey_response_results ()
    elif (option ==3):
        print ('exiting... ')
    else:
        print ('Invalid option...')