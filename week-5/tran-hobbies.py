"""
    Title: tran-hobbies.py
    Author: Phuong Tran
    Date: 02/08/2024
    Description: Python Lists.
"""
# a list of hobbies
hobbies = ["listening to music", "cooking", "reading", "relaxing", "sewing"]

# print each hobby to the console
for hobby in hobbies:
  print(hobby)

# a list of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# print a message according the day of the week
for day in days:
  if day == "Saturday" or day == "Sunday":
    print(day + ": No work today! Enjoy those hobbies!")
  else:
    print(day + ": It's a work day.")