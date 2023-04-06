
# This program calculates and displays travel expenses

# 4-6-2023

# CTI-110 P1HW1 - Travel Expense

# Tory Horton

#

print("This program calculates and displays travel expenses")

print()

Budget = input("Enter Budget: ")

Location = input("Enter your tavel destination: ")

print()

Fuel = input("How much do you think you will spend on gas? ")

Accomodation = input("Approximately, how much will you need for accomodation/hotel? ")

Food = input("Last, how much do you need for food? ")

print('------------Travel Expenses------------')

print()
print("Location: ", Location)
print("Initial Budget: ", Budget)

print()

print("Fuel: ", Fuel)
print("Accomodation: ", Accomodation)
print("Food: ", Food)

a = int(Budget)
b = int(Fuel)
c = int(Accomodation)
d = int(Food)
balance = a - b - c - d


print()

print("Remaining Balance: ",balance)

print()
