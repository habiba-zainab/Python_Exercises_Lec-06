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