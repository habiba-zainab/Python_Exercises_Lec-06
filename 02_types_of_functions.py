"""

=========================================================================
   LECTURE 06 - SET 02 :  TYPES OF FUNCTIONS
   Topics : Types of Functions - Built-in, User-defined, Lambda, Nested
   Total Questions :  08
=========================================================================

"""

# ==========================================================
# PART A:   Built-in vs User-defined Functions
# ==========================================================

# Q1: Built-in functions review
#    Demonstrate these built-in functions with examples:
#    len(), max(), min(), sum(), abs(), round(), sorted(), type()
#    Use a list of numbers for demonstration

print("\n--- Q1: Built-in Functions ---")

numbers = [45, 12, 78, 23, 67, 89, 34]
print("Numbers: ", numbers)
print()

print("len(): ", len(numbers))
print("max(): ", max(numbers))
print("min(): ", min(numbers))
print("sum(): ", sum(numbers))
print("abs(-5): ", abs(-5))
print("round(3.14159, 2): ", round(3.14159, 2))
print("sorted(): ", sorted(numbers))
print("type(): ", type(numbers))

# ----------------------------------------------------------

# Q2: User-defined function types
#    Create examples of:
#    - Function with no parameters, no return
#    - Function with parameters, no return
#    - Function with no parameters, with return
#    - Function with parameters and return

print("\n--- Q2: User-Defined Function Types ---")

def greet_basic() :
    print("Hello from function!")

def greet_name(name) :
    print("Hello, " + name + "!")

def get_current_year() :
    return 2024

def add_nums(a, b) :
    return a + b

print("1. No params, no return: ")
greet_basic()

print("\n2. With params, no return: ")
greet_name("Carl")

print("\n3. No params, with return: ")
print("Current year: ", get_current_year())

print("\n4. With params and return: ")
print("5 + 3 = ", add_nums(5, 3))

# ----------------------------------------------------------

# ==========================================================
# PART B: Lambda Functions & Functional Programming Tools
# ==========================================================

# Q3: Lambda function basics
#    Create lambda functions for:
#    - Square of a number
#    - Add two numbers
#    - Check if even
#    - Get absolute value
#    Call each and print results

print("\n--- Q3: Lambda Basics ---")

square = lambda x: x * x
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0
absolute = lambda x: abs(x)

print("Lambda Functions: ")
print("square(5): ", square(5))
print("add(3, 4): ", add(3, 4))
print("is_even(6): ", is_even(6))
print("is_even(7): ", is_even(7))
print("absolute(-10): ", absolute(-10))

# ----------------------------------------------------------

# Q4: Lambda with sorted()
#    Given: 
#           students = [('Alice', 85), ('Bob', 92),
#                     ('Charlie', 78)]
#    Sort by:
#    - Name (alphabetically)
#    - Marks (ascending)
#    - Marks (descending)
#    Use lambda as key

print("\n--- Q4: Lambda with sorted() ---")

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
print("Original: ", students)

by_name = sorted(students, key=lambda x: x[0])
by_marks_asc = sorted(students, key=lambda x: x[1])
by_marks_desc = sorted(students, key=lambda x: x[1], reverse=True)

print("\nSorted by name: ")
print(by_name)
print("\nSorted by marks (ascending): ")
print(by_marks_asc)
print("\nSorted by marks (descending): ")
print(by_marks_desc)

# ----------------------------------------------------------

# Q5: Lambda with map() and filter()
#    Given: 
#            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    Use map() to:
#    - Square each number
#    - Double each number
#    Use filter() to:
#    - Get even numbers
#    - Get numbers > 5

print("\n--- Q5: Lambda with map() & filter() ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Numbers: ", numbers)

squares = list(map(lambda x: x * x, numbers))
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
greater_than_5 = list(filter(lambda x: x > 5, numbers))

print("\nmap() - Squares: ", squares)
print("map() - Doubled: ", doubled)
print("\nfilter() - Evens: ", evens)
print("filter() - Greater than 5: ", greater_than_5)

# ----------------------------------------------------------

# Q6: Lambda with reduce()
#    Given: 
#            numbers = [1, 2, 3, 4, 5]
#    Use reduce() to:
#    - Find product of all numbers
#    - Find maximum number
#    - Concatenate list of strings

print("\n--- Q6: Lambda with reduce() ---")

from functools import reduce

nums_list = [1, 2, 3, 4, 5]
print("Numbers: ", nums_list)

product = reduce(lambda x, y: x * y, nums_list)
maximum_val = reduce(lambda x, y: x if x > y else y, nums_list)

words = ['Hello', 'World', 'Python']
concatenated = reduce(lambda x, y: x + ' ' + y, words)

print("Product: ", product)
print("Maximum: ", maximum_val)
print("\nWords: ", words)
print("Concatenated: ", "'" + concatenated + "'")

# ----------------------------------------------------------

# =============================================================
# PART C: Nested Functions, Closures, Higher-Order Architecture
# =============================================================

# Q7: Nested functions
#    Create outer function calculator() that contains:
#    - inner add(a, b)
#    - inner subtract(a, b)
#    - inner multiply(a, b)
#    - inner divide(a, b)
#    Outer function takes operation name and returns
#          inner function

print("\n--- Q7: Nested Functions ---")

def calculator(operation) :
    def add(a, b) :
        return a + b
    def subtract(a, b) :
        return a - b
    def multiply(a, b) :
        return a * b
    def divide(a, b) :
        return a / b if b != 0 else "Error: Division by Zero"

    if operation == "add" :
        return add
    elif operation == "subtract" :
        return subtract
    elif operation == "multiply" :
        return multiply
    elif operation == "divide" :
        return divide