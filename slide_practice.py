# Function Notation
# f(x) = 5x + 2
# x is considered our input, in the paranthesis f(x)
# Outputvalue woud be 5x + 2 calculated

# Functions (in Python): allow you to simplify
# a problem and/or reuse the same code. The action of
# creating a function is known as "procedureal abstraction"
# This all helps you organize your code


# f(x) = 5x + 2 rewritten as a Python function
def f(x):
	y = 5 * x + 2
	return y


# Every function starts with "def"
# Every function has a colon to end the first line
# Most functions have parameters (input, our example, is x)
# Every function has a name (here, ours is f)
# All lines of code inside the function are indented

# Using a function ("calling" a function)
# Find the y value associated with f(x) when x = 10
# f(10) = 5(10) + 2 = 52
# If you want an answer from a function, store it

y = f(10)
# 10 is my parameter (input)
# This will pass 10 through the function and return a value
print(y)

y1 = f(1)  # 7
y2 = f(2)  # 12
y3 = f(3)  # 17

# Functions must be defined BEFORE you call (use) them
# Usually functions go at the top of your program
# Examples of Functions


def example_1(x):
	ans = x**x
	return ans


e2 = example_1(2)  # = 4
e5 = example_1(5)  # = 3125
print(e5 - e2)  # = 3121


# Example of a fuction that cubes
def cube_it(x):
	ans = x * x * x
	return ans


cube_4 = cube_it(4)
print(cube_4)  # = 64


# Examples of a function that averages your grades
# 60% for tests, 30% fpr quizzes, 10% for others
def grade(test_avg, quiz_avg, other_avg):
	# Three parameters (inputs)
	total = (.60 * test_avg) + (.30 * quiz_avg) + (.10 * other_avg)
	return total


# Predict Mr P's six weeks grade in English
x = 96
y = 92
z = 100
# x, y, and z do not have to match the name of the parameters
six_weeks_grade = int(grade(x, y, z))
print("Mr. P's grade for the first six weeks is " + str(six_weeks_grade))

# We've done examples of Return Functions up until now
# Void Functions (Simple Functions)
# Functions are like recipies
# They will not execute until "Called" or "Invoked"


# Void Functions example one (no parameters)
def say_lots_of_stuff():
	print("Lots")
	print("of")
	print("Stuff")


# This function prints out "Lots of Stuff" on three lines
# Void Functions don't return anything, they just "do"

# When calling a function, you use its name
say_lots_of_stuff()

# The code within your function needs to be indented
# Functions are for organization
# Going forward, we will define functions at the top of our files

# Libraries
# Libraries are a directory of specific functions others have already made that we can use
# It lets us "reuse" code (saves time and effort)

# Random Library
# When using a library, you have to import it
import random

# Calling a function from library
# nameOfLibrary.nameOfFunction(parameters)
# Picks a random number between 1 and 100 (including 1 and 100)
print(random.randint(1, 100))
