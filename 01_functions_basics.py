"""

===========================================================================
   LECTURE 06 - SET 01 :  BASICS OF FUNCTIONS
   Topics : Function Basics - Defining, Calling, Parameters, Return Values
   Total Questions :  08
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

nums = [12, 45, 23, 67, 34]
print("Numbers: ", nums)

min_val, max_val, total_sum, avg_val = get_stats(nums)
print("Min: ", min_val)
print("Max: ", max_val)
print("Sum: ", total_sum)
print("Average: ", avg_val)

# ----------------------------------------------------------

# ==========================================================
# PART B:   Scope, Documentation, & Chaining
# ==========================================================

# Q5: Function with docstring
#    Create function is_even(number) with proper docstring
#    Docstring should explain: purpose, parameters, return
#    Print docstring using __doc__
#    Test with 5 numbers

print("\n--- Q5: Docstrings ---")

def is_even(number) :
    """
    Checks if a number is even.

    Parameters :
        number (int) : The number to check

    Returns :
        bool : True if even, False if odd
    """
    return number % 2 == 0

print("Function Documentation: ")
print(is_even.__doc__)

print("is_even(4): ", is_even(4))
print("is_even(7): ", is_even(7))
print("is_even(0): ", is_even(0))

# ----------------------------------------------------------

# Q6: Local vs Global variables
#    Demonstrate variable scope:
#    - Create global variable x = 10
#    - Create function that has local x = 20
#    - Show that global x is unchanged
#    - Use global keyword to modify global x

print("\n--- Q6: Variable Scope ---")

x = 10

def local_scope_test() :
    x = 20
    print("Local x inside function: ", x)

def global_scope_test() :
    global x
    x = 999

print("Global x before: ", x)
local_scope_test()
print("Global x after function: ", x, "(unchanged)")

print("\nUsing global keyword: ")
global_scope_test()
print("Global x after modification: ", x)

# ----------------------------------------------------------

# Q7: Function calling another function
#    Create:
#    - square(n) returns n*n
#    - cube(n) returns n*n*n
#    - power_table(n) calls square and cube, prints table

print("\n--- Q7: Function Chaining ---")

def square(n) :
    return n * n

def cube(n) :
    return n * n * n

def power_table(limit) :
    print("Power Table for 1 to " + str(limit) + ":")
    print("Number | Square | Cube")
    print("-----------------------")

    for i in range(1, limit + 1) :
        num_str = str(i).ljust(6)
        sq_str = str(square(i)).ljust(6)
        cu_str = str(cube(i))
        print(num_str + " | " + sq_str + " | " + cu_str)

power_table(5)

# ----------------------------------------------------------

# ==========================================================
# PART C:   Type Safety 
# ==========================================================

# Q8: Type checking in functions
#    Create function safe_divide(a, b) that:
#    - Checks if both are numbers
#    - Checks if b is not zero
#    - Returns result or error message

print("\n--- Q8: Type Checking ---")

def safe_divide(a, b) :

    if type(a) not in (int, float) or type(b) not in (int, float) :
        return "Error: Both arguments must be numbers"

    if b == 0 :
        return "Error: Cannot divide by zero"
    
    return a / b

print("safe_divide(10, 2): ", safe_divide(10, 2))
print("safe_divide(10, 0): ", safe_divide(10, 0))
print("safe_divide('10', 2): ", safe_divide("10", 2))
print("safe_divide(10, 3): ", safe_divide(10, 3))

# ----------------------------------------------------------