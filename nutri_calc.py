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

def convert_to_metric(weight, height, weight_unit, height_unit):
    if weight_unit.lower() == 'lbs':
        weight = weight * 0.453592                  # Convert lbs to kg
    
    if height_unit.lower() == 'feet and inches':
        feet = int(input("Enter feet: "))
        inches = int(input("Enter inches: "))
        height = (feet * 30.48) + (inches * 2.54)  # Convert feet and inches to cm
    
    return weight, height

# User input -- soon to be put into function.
gender = input("Enter gender (male/female): ")
weight_unit = input("Enter weight unit (kg/lbs): ")
height_unit = input("Enter height unit (cm/feet and inches): ")
weight = float(input(f"Enter weight ({weight_unit}): "))
height = float(input(f"Enter height ({height_unit}): "))
age = int(input("Enter age (years): "))
activity_level = input("Enter activity level (little, light, moderate, very active, extra active): ")

# Convert to metric if necessary
weight, height = convert_to_metric(weight, height, weight_unit, height_unit)

# Calculate BMR -- use all details to calculate BMR rounded.
bmr = calculate_bmr(gender, weight, height, age)
if bmr is None:
    print("Invalid gender input.")
else:
    total_calories = calculate_total_calories(bmr, activity_level)
    print(f"Your BMR is: {bmr:.2f} kcal/day")
    print(f"Your total daily calorie needs are: {total_calories:.2f} kcal/day")
