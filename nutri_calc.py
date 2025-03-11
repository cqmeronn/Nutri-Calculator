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
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    }
    
    return round(bmr * activity_multipliers.get(activity_level, 1.2), -2)

def get_valid_input(prompt, valid_options=None, value_type=str, condition=None):
    while True:
        try:
            user_input = value_type(input(prompt).strip().lower())
            if valid_options and user_input not in valid_options:
                print(f"Invalid input. Please enter one of the following: {', '.join(map(str, valid_options))}")
                continue
            if condition and not condition(user_input):
                print("Invalid input. Please enter a valid value.")
                continue
            return user_input
        except ValueError:
            print(f"Invalid input. Expected a {value_type.__name__}.")

def is_positive(value):
    return value > 0

def convert_to_metric(weight, height, weight_unit, height_unit):
    if weight_unit == 'lbs':
        weight = weight * 0.453592
    if height_unit == 'inches':
        height = height * 2.54
    return weight, height

def get_user_inputs():
    unit_system = get_valid_input("Choose unit system (metric/imperial): ", ['metric', 'imperial'])
    weight_unit = 'kg' if unit_system == 'metric' else 'lbs'
    height_unit = 'cm' if unit_system == 'metric' else 'inches'
    
    gender = get_valid_input("Enter gender (male/female): ", ['male', 'female'])
    weight = get_valid_input(f"Enter weight ({weight_unit}): ", value_type=float, condition=is_positive)
    height = get_valid_input(f"Enter height ({height_unit}): ", value_type=float, condition=is_positive)
    age = get_valid_input("Enter age (years): ", value_type=int, condition=is_positive)
    
    if unit_system == 'imperial':
        weight, height = convert_to_metric(weight, height, weight_unit, height_unit)
    
    activity_levels = {
        1: "Little/no exercise",
        2: "Light exercise",
        3: "Moderate exercise (3-5 days/wk)",
        4: "Very active (6-7 days/wk)",
        5: "Extra active (very active & physical job)"
    }
    
    print("Enter activity level:")
    for key, value in activity_levels.items():
        print(f"{key} - {value}")
    
    activity_level = get_valid_input("Choose a number (1-5): ", list(activity_levels.keys()), value_type=int)
    
    goals = {
        1: "Maintain weight",
        2: "Lose weight",
        3: "Gain weight"
    }
    
    print("Select your goal:")
    for key, value in goals.items():
        print(f"{key} - {value}")
    
    goal = get_valid_input("Choose a number (1-3): ", list(goals.keys()), value_type=int)
    
    weight_change = None
    if goal in [2, 3]:
        weight_change_options = {
            1: "0.25 kg (0.5 lbs)/week (mild change)",
            2: "0.5 kg (1 lbs)/week (moderate change)",
            3: "1 kg (2.2 lbs)/week (aggressive change)"
        }
        
        print(f"Select your weight {'loss' if goal == 2 else 'gain'} goal:")
        for key, value in weight_change_options.items():
            print(f"{key} - {value}")
        
        weight_change = get_valid_input("Choose a number (1-3): ", list(weight_change_options.keys()), value_type=int)
    
    return gender, weight, height, age, activity_level, goal, weight_change

def main():
    gender, weight, height, age, activity_level, goal, weight_change = get_user_inputs()
    bmr = calculate_bmr(gender, weight, height, age)
    if bmr is None:
        print("Invalid gender input.")
    else:
        total_calories = calculate_total_calories(bmr, activity_level)
        print(f"Your BMR is: {int(round(bmr, -2))} kcal/day")
        print(f"Your total daily calorie needs are: {int(round(total_calories, -2))} kcal/day")
        
        if goal == 2:  # Weight loss
            calorie_deficits = {1: 300, 2: 500, 3: 1100}
            total_calories -= calorie_deficits.get(weight_change, 0)
            print(f"To lose weight, you should consume around {int(round(total_calories, -2))} kcal/day.")
        elif goal == 3:  # Weight gain
            calorie_surpluses = {1: 300, 2: 500, 3: 1100}
            total_calories += calorie_surpluses.get(weight_change, 0)
            print(f"To gain weight, you should consume around {int(round(total_calories, -2))} kcal/day.")

if __name__ == "__main__":
    main()
