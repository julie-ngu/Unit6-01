# Created by: Julie Nguyen
# Created on: Nov 2017
# Created for: ICS3U
# This program is an example of enumerated types

from enum import Enum

# an enumerated name of days
Days = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

for days in Days:
    print(days)

print("\nNumber of days in a week: ")
print(len(Days))

day_selected = int(input('\nEnter the day # you like: '))

try:
    if Days[day_selected-1] in Days:
        print('\nYour favorite day of the week is: \n')
        print(Days[day_selected-1])
except:
    print('\nThat is not a valid number for a day in a week.')
