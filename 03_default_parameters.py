"""

==============================================================
   LECTURE 06 - SET 03 :   DEFAULT PARAMETERS
   Topics : Default Parameters, Keyword Args, *args, **kwargs
   Total Questions :  
==============================================================

"""

# ==========================================================
# PART A:   Parameter Shadows & Default Arguments
# ==========================================================

# Q1: Basic default parameters
#    Create function greet(name, greeting="Hello",
#               punctuation="!")
#    Call with:
#    - Only name
#    - Name and greeting
#    - All three parameters

print("\n--- Q1: Default Parameters ---")

def greet(name, greeting="Hello", punctuation="!") :
    print(greeting + " " + name + punctuation)

print('greet("Alice"): ')
greet("Alice")

print('\ngreet("Bob", "Hi"): ')
greet("Bob", "Hi")

print('\ngreet("Charlie", "Hey", "!!"): ')
greet("Charlie", "Hey", "!!")

# ----------------------------------------------------------

# Q2: Default parameter gotcha (mutable defaults)
#    Demonstrate the mutable default argument problem:
#    - Create function with default list parameter
#    - Call multiple times
#    - Show unexpected behavior
#    - Fix it using None as default

print("\n--- Q2: Mutable Default Gotcha ---")

def add_to_list_bad(val, target_list=[]) :
    target_list.append(val)
    return target_list