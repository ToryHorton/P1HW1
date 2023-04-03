
#This program calculates and displays travel expenses

#4-3-2023

#CTI-110 P1HW1 - Travel Expense

# Tory Horton

#Pseudocode

print("This program calculates and displays travel expenses")

print()

Budget = input("Enter Budget: ")

Location = input("Enter your tavel destination: ")

print()

Fuel = input("How much do you think you will spend on gas? ")

Accomodation = input("Approximately, how much will you need for accomodation/hotel? ")

Food = input("Last, how much do you need for food? ")

print()
Location = input("Location: ")
a = int(input("Initial Budget: "))

print()

b = int(input("Fuel: "))
c = int(input("Accomodation: "))
d = int(input("Food: "))

result = a - b - c - d

print()

print("Remaining Balance:",result)
