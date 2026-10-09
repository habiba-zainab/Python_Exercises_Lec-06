"""

==========================================================================
   LECTURE 06 - SET 01 :  BASICS OF FUNCTIONS
   Topics : Function Basics - Defining, Calling, Parameters, Return Values
   Total Questions :  
===========================================================================

"""

# ==========================================================
# PART A:   Basic Functions & Return Values
# ==========================================================

# Q1: Simple function - greet user
#    Create function greet(name) that prints "Hello, {name}!"
#    Call it with 3 different names

print("\n--- Q1: Simple Function ---")

def greet(name):
    print("Hello, " + name + "!")

greet("Elena")
greet("Eric")
greet("Carl")

# ----------------------------------------------------------

# Q2: Function with return value - add two numbers
#    Create function add(a, b) that returns sum
#    Store result in variable and print
#    Also print what happens if you don't use return

print("\n--- Q2: Return Value ---")

def add(a, b) :
    return a + b

def add_no_return(a, b) :
    result = a + b

sum1 = add(5, 3)
sum2 = add(10, 20)

print("add(5, 3) =", sum1)
print("add(10, 20) =", sum2)

no_return_val = add_no_return(10, 20)
print("Without return: ", no_return_val)

# ----------------------------------------------------------

# Q3: Function with multiple parameters
#    Create function calculate_area(length, width)
#    Returns area of rectangle
#    Call with different dimensions

print("\n--- Q3: Multiple Parameters ---")

def calculate_area(length, width) :
    return length * width

print("Rectangle 5 x 3: Area =", calculate_area(5, 3))
print("Rectangle 10 x 7: Area =", calculate_area(10, 7))
print("Rectangle 4.5 x 2.5: Area =", calculate_area(4.5, 2.5))

# ----------------------------------------------------------

# Q4: Function returning multiple values
#    Create function get_stats(numbers) that returns
#     min, max, sum, average as tuple
#    Unpack and print results

print("\n--- Q4: Multiple Return Values ---")

def get_stats(numbers) :
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    return minimum, maximum, total, average