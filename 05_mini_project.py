"""

============================================================
   LECTURE 06 - SET 05 :   MINI PROJECT
   Topics :       Functions and Recursions
============================================================

"""

# ==========================================================
#              FITNESS & HEALTH TRACKER
# ==========================================================

# ----------------------------------------------------------
#    STEP 01:     Basic Health Calculator
# ----------------------------------------------------------

print("\n---  Basic Health Calculator ---")

def calculate_bmi(weight, height) :
    """Calculate BMI from weight(kg) and height(m)"""
    bmi = weight / (height * height)
    return round(bmi, 1)

def daily_calories(weight, activity="moderate") :
    """Estimate daily calories (default: moderate)"""
    rates = {"low": 25, "moderate": 30, "high": 35}
    return weight * rates.get(activity, 30)

bmi = calculate_bmi(70, 1.75)
print("BMI: ", bmi)
print("Calories (moderate): ", daily_calories(70))
print("Calories (high): ", daily_calories(70, "high"))

# ----------------------------------------------------------
#    STEP 02:     Workout Statistics
# ----------------------------------------------------------

print("\n--- Workout Statistics ---")

def total_calories(*workouts) :
    """Sum all workout calories using *args"""
    total = 0
    for cal in workouts :
        total = total + cal
    return total

def workout_summary(**details) :
    """Display workout info using **kwargs"""
    print("  Workout Summary: ")
    for key, value in details.items() :
        print("    " + str(key) + ":", value)

print("Total burned: ", total_calories(300, 450, 200, 500), "cal")
workout_summary(type="Running", duration="30 min", calories=350)
