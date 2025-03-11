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
    weight_unit = weight_unit.lower()
    height_unit = height_unit.lower()
    
    if weight_unit not in ['kg', 'lbs']:
        raise ValueError("Invalid weight unit. Please enter 'kg' or 'lbs'.")
    if height_unit not in ['cm', 'feet and inches']:
        raise ValueError("Invalid height unit. Please enter 'cm' or 'feet and inches'.")
    
    if weight_unit == 'lbs':
        weight = weight * 0.453592                          # Convert lbs to kg
    
    if height_unit == 'feet and inches':
        while True:
            try:
                feet = int(input("Enter feet: "))
                inches = int(input("Enter inches: "))
                if feet < 0 or inches < 0:
                    print("Feet and inches must be non-negative.")
                    continue
                height = (feet * 30.48) + (inches * 2.54)   # Convert feet and inches to cm
                break
            except ValueError:
                print("Invalid input. Please enter numeric values for feet and inches.")
    
    return weight, height

# User input -- soon to be put into function.
while True:
    gender = input("Enter gender (male/female): ").strip().lower()
    if gender in ['male', 'female']:
        break
    print("Invalid gender. Please enter 'male' or 'female'.")

while True:
    weight_unit = input("Enter weight unit (kg/lbs): ").strip().lower()
    if weight_unit in ['kg', 'lbs']:
        break
    print("Invalid weight unit. Please enter 'kg' or 'lbs'.")

while True:
    height_unit = input("Enter height unit (cm/feet and inches): ").strip().lower()
    if height_unit in ['cm', 'feet and inches']:
        break
    print("Invalid height unit. Please enter 'cm' or 'feet and inches'.")

while True:
    try:
        weight = float(input(f"Enter weight ({weight_unit}): "))
        if weight > 0:
            break
        print("Weight must be a positive number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for weight.")

while True:
    try:
        height = float(input(f"Enter height ({height_unit}): "))
        if height > 0:
            break
        print("Height must be a positive number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for height.")

while True:
    try:
        age = int(input("Enter age (years): "))
        if age > 0:
            break
        print("Age must be a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for age.")

while True:
    activity_level = input("Enter activity level (little, light, moderate, very active, extra active): ").strip().lower()
    if activity_level in ['little', 'light', 'moderate', 'very active', 'extra active']:
        break
    print("Invalid activity level. Please choose from the given options.")

# Convert to metric if necessary
try:
    weight, height = convert_to_metric(weight, height, weight_unit, height_unit)
except ValueError as e:
    print(e)
    exit()

# Calculate BMR -- use all details to calculate BMR rounded.
bmr = calculate_bmr(gender, weight, height, age)
if bmr is None:
    print("Invalid gender input.")
else:
    total_calories = calculate_total_calories(bmr, activity_level)
    print(f"Your BMR is: {bmr:.2f} kcal/day")
    print(f"Your total daily calorie needs are: {total_calories:.2f} kcal/day")
