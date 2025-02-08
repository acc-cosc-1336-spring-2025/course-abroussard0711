#create decision functions

def get_options_ratio(options, total): #create function named get_options_ratio that accepts two parameters with names option, total and returns the ratio.
    ratio = options / total

    return (ratio)  #returns the ratio of options divided by total

# create function named get_faculty_rating that returns a faculty score according the five if decision parameters 
def get_faculty_rating (ratio):
    if (ratio <= 1 and ratio >= .9):
        return 'Excellent'
    if (ratio < .9 and ratio >= .8):
        return 'Very Good'
    if (ratio < .8 and ratio >= .7):
        return 'Good'
    if (ratio < .7 and ratio >= .6):
        return 'Needs Improvement'
    if (ratio < .6 and ratio >= 0):
        return 'Unacceptable'
