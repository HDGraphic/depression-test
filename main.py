# Importing the required libraries
import time

# Displaying the instructions
print("Welcome to the depression detection test")
print('Please answer the following questions using a scale of 0 to 3, where 0 = Never, 1 = Several days, 2 = half the days or more, 3 = Almost every day.\n")

# Declaring the score variable
score = 0

# Looping through the questions
for i, question in enumerate(questions):
    answer = int(input(f"{i+1}. {question} "))
    score += answer
