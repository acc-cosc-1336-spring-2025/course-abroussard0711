# functions to determine the hours, minutes, and seconds

# to calculate the number of hours
def get_hour(epoch_seconds):
    result = epoch_seconds // 3600
    remainder = result % 24
    return remainder

# to calculate the number of minutes
def get_minutes (epoch_seconds):
    result = epoch_seconds // 60
    remainder = result % 60
    return remainder

# to calculate the number of seconds
def get_seconds (epoch_seconds):
    result = epoch_seconds % 3600
    remainder = result % 60
    return remainder