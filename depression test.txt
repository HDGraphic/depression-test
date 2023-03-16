# Importing the required libraries
import time

# Displaying the instructions
print("Please answer the following questions with a number from 0 to 3, where")
print("0 = not at all, 1 = several days, 2 = more than half the days, and 3 = nearly every day.\n")

# Declaring the score variable
score = 0

# Looping through the questions
for i, question in enumerate(questions):
    answer = int(input(f"{i+1}. {question} "))
    score += answer
