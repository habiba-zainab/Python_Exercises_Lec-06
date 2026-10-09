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
