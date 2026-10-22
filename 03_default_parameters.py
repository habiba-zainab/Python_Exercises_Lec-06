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

def add_to_list_good(val, target_list=None) :
    if target_list is None :
        target_list = []
    target_list.append(val)
    return target_list

print("BAD (mutable default): ")
print("Call 1: ", add_to_list_bad(1))
print("Call 2: ", add_to_list_bad(2))
print("Call 3: ", add_to_list_bad(3))

print("\nGOOD (None default): ")
print("Call 1: ", add_to_list_good(1))
print("Call 2: ", add_to_list_good(2))
print("Call 3: ", add_to_list_good(3))

# ----------------------------------------------------------

# ==========================================================
# PART B:   Position-Specific & Keyword Signatures
# ==========================================================

# Q3: Keyword arguments
#    Create function create_profile(name, age, city, job)
#    Call using keyword arguments in different orders

print("\n--- Q3: Keyword Arguments ---")

def create_profile(name, age, city, job) :
    print("Profile: name=" + name + ", age=" + str(age) + ", city=" + city + ", job=" + job)

print("Calling with standard ordering: ")
create_profile(name="Alice", age=25, city="NYC", job="Engineer")

print("\nCalling with mixed keyword ordering: ")
create_profile(job="Designer", city="LA", age=30, name="Bob")

# ----------------------------------------------------------

# Q4: Mixing positional and keyword arguments
#    Create function 
#           order_pizza(size, crust="regular", *toppings)
#    Call with different combinations

print("\n--- Q4: Mixed Arguments ---")

def order_pizza(size, crust="regular", *toppings) :
    print("Size: ", size, "| Crust: ", crust, end=" ")
    if toppings :
        print(" | Toppings: ", ", ".join(toppings))
    else :
        print(" | No extra toppings")

order_pizza("Large")
order_pizza("Medium", "thin", "cheese", "mushroom")
order_pizza("Small", "thick", "pepperoni", "olive", "onion")

# ----------------------------------------------------------

# Q5: Function with all parameter types
#    Create function that uses ALL parameter types:
#    def full_demo(pos1, pos2, /, normal, 
#                      *args, kwonly=True, **kwargs)
#    (Simplified version for beginners)
#    Demonstrate each type

print("\n--- Q5: All Parameter Types ---")

def full_demo(pos1, pos2, /, normal, *args, kwonly=True, **kwargs) :
    print("Positional: ", pos1, ",", pos2)
    print("Normal: ", normal)
    print("*args: ", args)
    print("Keyword-only: ", kwonly)
    print("**kwargs: ", kwargs)

full_demo(1, 2, 3, 4, 5, kwonly=False, extra="value", bonus=100)

# ----------------------------------------------------------

# ==========================================================
# PART C:   Dynamics Unbound Parameters(*args & kwargs)
# ==========================================================

# Q6: *args - variable positional arguments
#    Create function sum_all(*args) that:
#    - Accepts any number of arguments
#    - Returns their sum
#    - Prints how many numbers were passed

print("\n--- Q6: *args ---")

def sum_all(*args) :
    total = sum(args)
    count = len(args)
    return total, count

print("sum_all(1, 2, 3): ", sum_all(1, 2, 3)[0], "(" + str(sum_all(1, 2, 3)[1]) + " numbers)")
print("sum_all(10, 20, 30, 40): ", sum_all(10, 20, 30, 40)[0], "(" + str(sum_all(10, 20, 30, 40)[1]) + " numbers)")
print("sum_all(5): ", sum_all(5)[0], "(" + str(sum_all(5)[1]) + " number)")
print("sum_all(): ", sum_all()[0], "(" + str(sum_all()[1]) + " numbers)")

# ----------------------------------------------------------

# Q7: **kwargs - variable keyword arguments
#    Create function print_info(**kwargs) that:
#    - Accepts any keyword arguments
#    - Prints each key-value pair formatted

print("\n--- Q7: **kwargs ---")

def print_info(**kwargs) :
    print("─" * 20)
    for key, val in kwargs.items() :
        print(key + ":", val)
    print("─" * 20)

print_info(name="Alice", age=25, city="NYC")
print_info(product="Laptop", price=999, brand="Dell")

# ----------------------------------------------------------