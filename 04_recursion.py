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