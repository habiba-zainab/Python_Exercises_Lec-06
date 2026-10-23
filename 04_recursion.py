"""

============================================================
   LECTURE 06 - SET 04 :   RECURSIONS
   Topics : Recursion - Basics, Classic Problems
   Total Questions :  
============================================================

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

print("\n--- Q3: Reverse String ---")

def reverse_string(s) :
    if len(s) <= 1 :
        return s
    return s[-1] + reverse_string(s[:-1])

print('reverse_string("Hello") = ', '"' + reverse_string("Hello") + '"')
print('reverse_string("Python") = ', '"' + reverse_string("Python") + '"')
print('reverse_string("A") = ', '"' + reverse_string("A") + '"')

print('\nSteps for reverse_string("Hello"): ')
print('"Hello" -> "o" + reverse("Hell")')
print('"Hell"  -> "l" + reverse("Hel")')
print('"Hel"   -> "l" + reverse("He")')
print('"He"    -> "e" + reverse("H")')
print('"H"     -> "H" (base case)')
print('Result: "' + reverse_string("Hello") + '"')

# ----------------------------------------------------------

# ==========================================================
# PART B:   Mathematical Recursion
# ==========================================================

# Q4: Palindrome check using recursion
#    Create function is_palindrome(s)
#    Check by comparing first and last characters

print("\n--- Q4: Palindrome Check ---")

def is_palindrome(s) :
    if len(s) <= 1 :
        return True
    if s[0] != s[-1] :
        return False
    return is_palindrome(s[1:-1])

print('is_palindrome("radar"): ', is_palindrome("radar"))
print('is_palindrome("hello"): ', is_palindrome("hello"))
print('is_palindrome("madam"): ', is_palindrome("madam"))
print('is_palindrome("racecar"): ', is_palindrome("racecar"))

print('\nSteps for is_palindrome("radar"): ')
print("'r' == 'r' -> check 'ada'")
print("'a' == 'a' -> check 'd'")
print("'d' -> single char -> True")

# ----------------------------------------------------------

# Q5: Sum of list using recursion
#    Create function recursive_sum(lst)
#    Sum all elements without using loop

print("\n--- Q5: Recursive Sum ---")

def recursive_sum(lst) :
    if len(lst) == 0 :
        return 0
    if len(lst) == 1 :
        return lst[0]
    return lst[0] + recursive_sum(lst[1:])

print("recursive_sum([1, 2, 3, 4, 5]) = ", recursive_sum([1, 2, 3, 4, 5]))
print("recursive_sum([10, 20, 30]) = ", recursive_sum([10, 20, 30]))
print("recursive_sum([]) = ", recursive_sum([]))

print("\nSteps for [1, 2, 3, 4, 5]: ")
print("1 + recursive_sum([2, 3, 4, 5])")
print("1 + 2 + recursive_sum([3, 4, 5])")
print("1 + 2 + 3 + recursive_sum([4, 5])")
print("1 + 2 + 3 + 4 + recursive_sum([5])")
print("1 + 2 + 3 + 4 + 5 = 15")

# ----------------------------------------------------------