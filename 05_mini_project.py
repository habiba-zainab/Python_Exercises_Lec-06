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