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
    
    return bmr * activity_multipliers.get(activity_level, 1.2)

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

def get_user_inputs():
    gender = get_valid_input("Enter gender (male/female): ", ['male', 'female'])
    weight = get_valid_input("Enter weight (kg): ", value_type=float, condition=is_positive)
    height = get_valid_input("Enter height (cm): ", value_type=float, condition=is_positive)
    age = get_valid_input("Enter age (years): ", value_type=int, condition=is_positive)
    
    print("Enter activity level:")
    print("1 - Little/no exercise")
    print("2 - Light exercise")
    print("3 - Moderate exercise (3-5 days/wk)")
    print("4 - Very active (6-7 days/wk)")
    print("5 - Extra active (very active & physical job)")
    
    activity_level = get_valid_input("Choose a number (1-5): ", [1, 2, 3, 4, 5], value_type=int)
    
    return gender, weight, height, age, activity_level

def main():
    gender, weight, height, age, activity_level = get_user_inputs()
    bmr = calculate_bmr(gender, weight, height, age)
    if bmr is None:
        print("Invalid gender input.")
    else:
        total_calories = calculate_total_calories(bmr, activity_level)
        print(f"Your BMR is: {bmr:.2f} kcal/day")
        print(f"Your total daily calorie needs are: {total_calories:.2f} kcal/day")

if __name__ == "__main__":
    main()
