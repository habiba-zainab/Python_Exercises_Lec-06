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

def add(a, b) :
    return a + b

def add_no_return(a, b) :
    result = a + b

sum1 = add(5, 3)
sum2 = add(10, 20)

print("add(5, 3) =", sum1)
print("add(10, 20) =", sum2)

