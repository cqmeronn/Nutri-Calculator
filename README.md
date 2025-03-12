# BMR and Calorie Calculator

## Description

This Python script calculates the Basal Metabolic Rate (BMR) and estimates daily calorie needs based on user input. The script runs in interactive mode, asking for user input step by step to determine calorie needs based on activity level and goals.

## Features

- Supports both **metric** and **imperial** unit systems.
- Calculates **BMR** based on weight, height, age, and gender.
- Estimates **daily calorie needs** based on activity level.
- Provides options for **weight maintenance, loss, or gain.**
- Validates all inputs and prompts again if invalid values are entered.

## Requirements

- Python 3.7 or higher

## Installation

No external dependencies are required. Simply clone the repository or download `nutri_calc.py` and run it with Python.

```sh
python nutri_calc.py
```

## Usage

### Interactive Mode

Run the script without arguments to enter values manually:

```sh
python nutri_calc.py
```

The script will ask for:

1. **Unit system** (metric/imperial)
2. **Gender** (male/female)
3. **Weight**
4. **Height**
5. **Age**
6. **Activity level**
7. **Goal** (maintain, lose, gain weight)
8. **Weight change goal** (for weight loss/gain)

### Handling Invalid Inputs

If an invalid value is entered, the script will notify the user and ask for the input again. Example:

```sh
Enter age (years): abc
Sorry, "abc" is not a valid age.
Enter age (years):
```

## Example Output

```
Enter weight (kg): 70
Enter height (cm): 175
Enter age (years): 25
Enter activity level:
1 - Little/no exercise
2 - Light exercise
3 - Moderate exercise (3-5 days/wk)
4 - Very active (6-7 days/wk)
5 - Extra active (very active & physical job)
Choose a number (1-5): 3

Select your goal:
1 - Maintain weight
2 - Lose weight
3 - Gain weight
Choose a number (1-3): 2

Your BMR is: 1700 kcal/day
Your total daily calorie needs are: 2200 kcal/day
To lose weight, you should consume around 1700 kcal/day.
```
