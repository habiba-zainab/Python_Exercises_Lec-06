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

# ----------------------------------------------------------
#    STEP 03:     Diet & Meal Planner
# ----------------------------------------------------------

print("\n--- Diet & Meal Planner ---")

meals = [
    {"name": "Salad", "cal": 200},
    {"name": "Chicken", "cal": 400},
    {"name": "Rice", "cal": 300},
    {"name": "Soup", "cal": 150},
    {"name": "Steak", "cal": 500}
]

# Filter low-calorie meals (under 350) using lambda
low_cal = list(filter(lambda m: m["cal"] < 350, meals))
print("Low-calorie meals: ")
for m in low_cal :
    print("  " + m["name"] + " -", m["cal"], "cal")


# Sort meals by calories using lambda
sorted_meals = sorted(meals, key=lambda m: m["cal"])
print("Sorted by calories: ")
for m in sorted_meals :
    print("  " + m["name"] + " -", m["cal"], "cal")

# ----------------------------------------------------------
#    STEP 04:     Progress Tracker
# ----------------------------------------------------------

print("\n--- Progress Tracker ---")

def weekly_total(days, index=0) :
    """Recursively sum weekly calories burned"""
    if index == len(days) :
        return 0
    return days[index] + weekly_total(days, index + 1)

def count_streak(completed, index=0) :
    """Recursively count consecutive workout days"""
    if index == len(completed) or not completed[index] :
        return 0
    return 1 + count_streak(completed, index + 1)

week = [300, 450, 0, 200, 500, 350, 400]
streak = [True, True, True, False, True, True, False]

print("Weekly total: ", weekly_total(week), "cal")
print("Current streak: ", count_streak(streak), "days")