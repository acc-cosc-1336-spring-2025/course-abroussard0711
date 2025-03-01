# to run the functions of epoch time

import value_return

# main program to call the hour, minutes, and seconds return functions and display formatted outputs in HH:MM:SS
def main():
   epoch_time = 3800
   hours = value_return.get_hour(epoch_time)
   minutes = value_return.get_minutes(epoch_time)
   seconds = value_return.get_seconds(epoch_time)

   print (f'Time: {hours:02}:{minutes:02}:{seconds:02}')

main ()

