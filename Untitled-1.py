#######################################################################################################################################################
# 
# Name:MANN RAMNANI 
# SID:750001476
# Exam Date: 28 march 2024
# Module: programming for business analytics
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-friday-mr9971
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Data Processing and Loops
# You are given a string representing customer reviews. Use a for loop to process the text and count occurrences of specific keywords.
# Your allocated keywords are determined by the first and last digit of your SID.
# Count and store occurrences of each keyword in a dictionary called keyword_counts.
 
customer_reviews = """The product is well-designed and user-friendly. However, I experienced some issues with durability. The customer service was helpful, 
but I expected a faster response. The quality of the materials used is excellent. Overall, the purchase was satisfactory."""

# Keywords dictionary
keywords = {
    0: 'user-friendly',
    1: 'helpful',
    2: 'durability',
    3: 'response',
    4: 'satisfactory',
    5: 'quality',
    6: 'service',
    7: 'issues',
    8: 'purchase',
    9: 'materials'
}

# Write your code to process the text and count keyword occurrences

#defining SID first and last digit
first_digit = 7
last_digit = 6

#creating a new list 
my_list = []

#inintiating a loop for finctioning 
for word in customer_reviews.lower().split():
    #checking if the word is in the keywords dictionary
    if word in keywords.values():
        #adding the word to the list
        my_list.append(word)
        
#creating a dictionary to store the keywords and their counts
keyword_counts = {}
#starting a loop for counting keywords
for keyword in keywords.values():
    #counting the occurrences of each keyword
    keyword_counts[keyword] = my_list.count(keyword)
    
# printing the keyword counts
print("keyword counts:", keyword_counts)


#the outout of the code is:
# Keyword Counts: {'user-friendly': 1, 'helpful': 1, 'durability': 1, 'response': 0, 'satisfactory': 1, 'quality': 1, 'service': 0, 'issues': 0, 'purchase': 0, 'materials': 0}

##########################################################################################################################################################

# Question 2 - Business Metrics
# Scenario - You work in an online retail company as a business analyst. Your manager wants weekly reports on financial performance, including:
# Gross Profit Margin, Inventory Turnover, Customer Retention Rate (CRR), and Break-even Analysis. Implement Python functions 
# that take relevant values as inputs and return the computed metric. Use the first two and last two digits of your ID number as input values.

# Insert first two digits of ID number here:75
# Insert last two digits of ID number here:76

# Write your function for Gross Profit Margin
#defining gross profit margin 
def gross_profit_margin(revenue, cost_of_goods_sold):
    """Calculate Gross Profit Margin as a percentage."""
    # Check if revenue is not zero to avoid division by zero error
    if revenue == 0 :
        return 0
    # Calculate gross profit
    gross_profit = revenue - cost_of_goods_sold
    # Return gross profit margin as a percentage
    return (gross_profit / revenue) * 100



# Write your function for Inventory Turnover
#defining inventory turnover
def inventory_turnover(cost_of_goods_sold, average_inventory):
    """calculate inventory ratio."""
    # checking if average inventory is not equal to zero 
    if average_inventory == 0:
        return 0
    # calculate inventory ratio
    return cost_of_goods_sold / average_inventory


# Write your function for Customer Retention Rate (CRR)
#defining customer retention rate
def customer_retention_rate(customers_at_start, customers_at_end):
    """calculate customer retention rate (crr) as a percentage."""
    # Check if customers at start is not zero to avoid division by zero error
    if customers_at_start == 0:
        return 0
    # Calculate customer retention rate
    return (customers_at_end  / customers_at_start) * 100


# Write your function for Break-even Analysis
#defining break-even analysis
def break_even_analysis(fixed_costs, selling_price_per_unit, variable_cost_per_unit):
    """calculate Break-even Point in units."""
    # checking if selling price per unit is not equal to variable cost per unit to avoid division by zero error
    if selling_price_per_unit - variable_cost_per_unit == 0 :
        return float('inf')  #float represents infinity
    # Calculate break-even point
    return fixed_costs / (selling_price_per_unit - variable_cost_per_unit)

# Call your functions here
#defining the values
#given id number is 75 and 76

#defining the values
revenue = 75
cost_of_goods_sold = 76
average_inventory = 75
customers_at_start = 76
customers_at_end = 75
fixed_costs = 76
selling_price_per_unit = 75
variable_cost_per_unit = 76

# initializing the functions to define and calculate the gorss proft margin, inventory, customer rate and break-even analysis
print ("gross profit margin is:", gross_profit_margin(revenue, cost_of_goods_sold))
print ("inventory is:", inventory_turnover(cost_of_goods_sold, average_inventory))
print ("customer retention rate is:", customer_retention_rate(customers_at_start, customers_at_end))
print ("break-even analysis is:", break_even_analysis(fixed_costs, selling_price_per_unit, variable_cost_per_unit))

# output received is given as follows 
# gross profit margin is: -1.333333
# inventory is: 1.013333
# customer rate is: 98.684210
# break-even analysis is: -76.0



##########################################################################################################################################################

# Question 3 - Forecasting and Regression
# A logistics company has gathered data on delivery costs and shipment volumes. The table below provides different costs and their corresponding shipment volumes.
# Develop a linear regression model and determine:
# 1. The optimal delivery cost that maximizes profit
# 2. The expected shipment volume when the cost is set at £68

"""
Delivery Cost (£)    Shipment Volume (Units)
-------------------------------------------
25                  500
30                  480
35                  450
40                  420
45                  400
50                  370
55                  340
60                  310
65                  290
70                  250
"""

# Write your regression model code here


#importing all the necessary libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#now defining the data
cost = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1) #reshaping the data 
volume = np.array([500, 480, 450, 420, 400, 370, 340, 310, 290, 250])

#creating a linear regression model
model = LinearRegression()
#fitting the model with the data
model.fit(cost, volume)

#predicting the shipment volume
predicted_volume = model.predict(np.array([[68]]))[0] #predicting the shipment volume when cost is set at 68



# finding optimal delivery cost 
# assuming profit = revenue - cost, and revenue = volume * price per unit 
profits = volume - cost.flatten() 
optimal_index = np.argmax(profits) 
optimal_cost = cost[optimal_index][0]

# Plotting the data and regression line
plt.scatter(cost, volume, color='blue', label='Data Points')
plt.plot(cost, model.predict(cost), color='red', label='Regression Line')
plt.xlabel('Delivery Cost (£)')
plt.ylabel('Shipment Volume (Units)')
plt.title('Delivery Cost vs Shipment Volume')
plt.legend()
plt.grid()
plt.show()

# Output generated 

##########################################################################################################################################################

# Question 4 - Debugging and Data Visualization

import random as random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student ID number
your_ID=input("Enter your Student ID:750001476 ")
max_value = int(your_ID)
random_numbers = [random.randint(your_ID, max_value) in range(100)]

# Plotting the numbers in a histogram
plt.hist(random_numbers, bin=10, edgecolour='blue', alpha=0.7, colour='red')
plt.title("Histogram of 100 Random Numbers")
plt.xlabel("Value Range")
plt.ylabel9("Frequency")
plt.grid("True")
plt.show("plot")

