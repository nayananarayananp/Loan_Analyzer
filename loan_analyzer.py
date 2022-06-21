# coding: utf-8
from pathlib import Path
import csv

#Part 1: Automate the Calculations.
#Automate the calculations for the loan portfolio summaries.

loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list? Print
number_of_loans = len(loan_costs)
print (f"The total number of loans in the list: {number_of_loans}")

# What is the total of all loans?
total_of_loans = sum(loan_costs)
print (f"The total value of all loans in the list: {total_of_loans}")

# What is the average loan amount from the list?

# average = sum of loans / number of loans
average_loan_price = (total_of_loans/number_of_loans)
print (f"The average loan price is: {average_loan_price}")

# Part 2: Analyze Loan Data.
# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
# Using get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.

# get future value
future_value= loan.get("future_value")
print (f"The future value of the loan is: {future_value}")

# get remaning months
remaining_months= loan.get("remaining_months")
print (f"The remaining months of the loan is: {remaining_months}")

#Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
discount_rate = 0.20

#calculate present value
present_value = future_value / (1 + discount_rate/12) ** remaining_months
print (f"The present value of the loan is: {present_value}")

#Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
loan_price = loan.get("loan_price")
print (f"The loan price of the loan is: {loan_price}")

# condition to check present value against loan price
if present_value >= loan_price:
    print ("the loan is worth at least the cost to buy it.")
elif present_value < loan_price:
    print ("the loan is too expensive and not worth the price.")

#Part 3: Perform Financial Calculations.
#Define a new function that will be used to calculate present value. 
# The function should have parameters Future_Values, Discount_Rate, Remaining_Months and print present value 
def calculate_present_value (future_value, discount_rate, remaining_months):
    present_value = future_value / (1 + discount_rate/12) ** remaining_months
    print (f"The present value of the loan is: {present_value}")
    return present_value

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
# Use the function to calculate the present value of the new loan given below.
# Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# get loan price
loan_price= new_loan.get("loan_price")
print (f"The loan price of the loan is: {loan_price}")
annual_discount_rate = 0.20

# calculate using function
calculate_present_value (1000,annual_discount_rate,12)


#Part 4: Conditionally filter lists of loans.

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]
# Create a new, empty list called `inexpensive_loans`.
inexpensive_loans = []

# Use a for loop to select each loan from a list of loans.
#a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
#b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
#c. Print 'inexpensive_loans'

for my_loan in loans:
    if my_loan.get("loan_price") <= 500:
        # add to list only if condition is met
        inexpensive_loans.append (my_loan)
print("Inexpensive loans are: ",inexpensive_loans)

# Part 5: Save the results.
# Set the output file path
csvpath = Path("inexpensive_loans.csv")
print ("This is the absolute path: ", csvpath.absolute()) 
print ("This is the relative path: ", csvpath) 

# Create a `csvwriter` using the `csv` library. Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Use `with open` to open a new CSV file. Output this list of inexpensive loans to a csv file
with open('inexpensive_loans.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for loan in inexpensive_loans:
        writer.writerow(loan.values())