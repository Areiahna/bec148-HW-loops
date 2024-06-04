# Task 1: Every Other Day 
# Write a program that prints each day of the week, but only if that day is on an even index.

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for day in range(1,len(days_of_week)):
    if (day % 2 == 0):
        print(days_of_week[day])