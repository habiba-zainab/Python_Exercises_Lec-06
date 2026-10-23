"""

==============================================================
   LECTURE 06 - SET 04 :   RECURSIONS
   Topics : Recursion - Basics, Classic Problems, Advanced
   Total Questions :  
==============================================================

"""

# ==========================================================
# PART A:   Basic Recursion Patterns
# ==========================================================

# Q1: Factorial using recursion
#    Create function factorial(n)
#    Show step-by-step calculation
#    Handle base case (0! = 1)

print("\n--- Q1: Factorial ---")

def factorial(n) :
    if n == 0 or n == 1 :
        return 1
    return n * factorial(n - 1)

print("factorial(0) = ", factorial(0))
print("factorial(5) = ", factorial(5))
print("factorial(10) = ", factorial(10))

print("\nStep-by-step for factorial(5): ")
print("5! = 5 x 4!")
print("   = 5 x 4 x 3!")
print("   = 5 x 4 x 3 x 2!")
print("   = 5 x 4 x 3 x 2 x 1!")
print("   = 5 x 4 x 3 x 2 x 1")
print("   =", factorial(5))

# ----------------------------------------------------------

# Q2: Fibonacci using recursion
#    Create function fibonacci(n)
#    Print first 10 Fibonacci numbers
#    Show recursive calls for small number

print("\n--- Q2: Fibonacci ---")

def fibonacci(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("fibonacci(0) = ", fibonacci(0))
print("fibonacci(1) = ", fibonacci(1))
print("fibonacci(5) = ", fibonacci(5))

print("\nFirst 10 Fibonacci numbers: ")
fib_list = []
for i in range(10) :
    fib_list.append(str(fibonacci(i)))
print(", ".join(fib_list))

# ----------------------------------------------------------

# Q3: Reverse string using recursion
#    Create function reverse_string(s)
#    Show step-by-step reversal