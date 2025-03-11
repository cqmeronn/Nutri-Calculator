"""Calculator to determine user's BMI and nutritional requirements from their height and weight."""

def calculate_bmr(gender, weight, height, age):
    if gender.lower() == 'male':
        return 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    elif gender.lower() == 'female':
        return 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
    else:
        return None

def calculate_total_calories(bmr, activity_level):
    activity_multipliers = {
        'little': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }
    
    return bmr * activity_multipliers.get(activity_level.lower(), 1.2)

# User input -- soon to be put into function.
gender = input("Enter gender (male/female): ")
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (cm): "))
age = int(input("Enter age (years): "))
activity_level = input("Enter activity level (little, light, moderate, very active, extra active): ")

# Calculate BMR -- use all detaisl to calculate BMR rounded.
bmr = calculate_bmr(gender, weight, height, age)
if bmr is None:
    print("Invalid gender input.")
else:
    total_calories = calculate_total_calories(bmr, activity_level)
    print(f"Your BMR is: {bmr:.2f} kcal/day")
    print(f"Your total daily calorie needs are: {total_calories:.2f} kcal/day")
