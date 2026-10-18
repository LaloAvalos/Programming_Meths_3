# =============================================================================
# FRONT PAGE
# =============================================================================
# Name:       Eduardo Avalos Lopez
# Student ID: 2630375
# Group:      TSU-75018 (IM-103)
# Assignment: Programming Methodology
# =============================================================================

# =============================================================================
# EXECUTIVE SUMMARY
# =============================================================================
# int stores whole numbers (age, hours, items) and float stores numbers with
# decimals (temperature, salary, bmi). They differ in precision and in how
# they are used: int is exact, while float can have small rounding errors.
# A boolean (bool) has only two values, True and False. It is usually obtained
# from a comparison (x >= 30.0) or from combining other booleans with and/or/not.
# Validating ranges and avoiding division by zero is important because invalid
# values (negative hours, zero income) produce wrong results or crash the
# program with ZeroDivisionError.
# This document covers six problems: temperature conversion, overtime pay,
# discount eligibility, statistics of three integers, loan eligibility and BMI.
# Each one defines its inputs, outputs, validations and three test cases, and
# uses int, float and bool to make simple decisions.
# The program runs the six problems in order; each one asks for its data with
# input() and decides what to show using if / else.

# =============================================================================
# PRINCIPLES AND GOOD PRACTICES
# =============================================================================
# - Use appropriate types: int for counters, float for values with decimals.
# - Avoid repeating complex expressions: store intermediate results in
#   variables (regular_pay, overtime_pay, debt_ratio, ...).
# - Validate data before operating (no negative hours or salaries).
# - Use descriptive variable names and clear messages for the user.
# - Document what true and false mean in each context:
#     is_high_temperature: true  = temp_c is 30.0 or more
#     has_overtime:        true  = more than 40 hours were worked
#     discount_eligible:   true  = at least one discount rule is met
#     all_even:            true  = the three numbers are even
#     eligible (loan):     true  = income, debt ratio and score all pass
#     is_underweight / is_normal / is_overweight: true = bmi is in that range
# - Text is checked character by character (for + range + "in") BEFORE it is
#   converted with float() or int(), so invalid text never crashes the program.
# - Tools used: print, input, len, range, str, int, float, round, min, max,
#   strip, upper, lower, list append, f-strings and if / elif / else.

# -----------------------------------------------------------------------------
# Constants (UPPER_SNAKE_CASE)
# -----------------------------------------------------------------------------
ERROR_MESSAGE = "Error: invalid input"
DIGITS = "0123456789"
HIGH_TEMPERATURE_LIMIT_C = 30.0
KELVIN_OFFSET = 273.15
REGULAR_HOURS_LIMIT = 40.0
OVERTIME_MULTIPLIER = 1.5
DISCOUNT_RATE = 0.10
DISCOUNT_MIN_PURCHASE = 1000.0
VALID_ANSWERS = ["YES", "NO"]
MIN_LOAN_INCOME = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650
UNDERWEIGHT_LIMIT = 18.5
OVERWEIGHT_LIMIT = 25.0
DECIMALS = 2

# How the number check works in every problem (explained once here):
#   - Each text may contain digits, at most max_dots '.' characters, and a
#     '-' only as the very first character.
#   - It must contain at least one digit (so "-" or "." alone are rejected).
#   - max_dots is 1 for float values and 0 for int values.


# =============================================================================
# Problem 1: Temperature converter and range flag
# =============================================================================
# Description:
#   Converts a temperature from Celsius to Fahrenheit and Kelvin. It also
#   gives a boolean is_high_temperature that is true when temp_c >= 30.0.
#
# Inputs:
#   - temp_c (float; temperature in Celsius)
#
# Outputs:
#   - "Fahrenheit: <temp_f>"
#   - "Kelvin: <temp_k>"
#   - "High temperature: true|false"
#
# Validations:
#   - temp_c can be converted to float.
#   - Kelvin cannot be negative (temp_k >= 0.0).
#
# Test cases:
#   1) Normal: 25 -> Fahrenheit 77.0, Kelvin 298.15, High temperature false
#   2) Border: 30.0 -> Fahrenheit 86.0, Kelvin 303.15, High temperature true
#   3) Error:  "abc" (not a number) or -300 (Kelvin below zero) -> error
print("=== Problem 1: Temperature converter ===")
temp_text = input("Enter temperature in Celsius: ").strip()

numeric_texts = [temp_text]
max_dots_list = [1]
all_numbers = True
for position in range(len(numeric_texts)):
    text = numeric_texts[position]
    dot_count = 0
    digit_count = 0
    for index in range(len(text)):
        character = text[index]
        if character in DIGITS:
            digit_count += 1
        elif character == ".":
            dot_count += 1
        elif character != "-" or index != 0:
            all_numbers = False
    if digit_count == 0 or dot_count > max_dots_list[position]:
        all_numbers = False

if all_numbers:
    temp_c = float(temp_text)
    temp_k = temp_c + KELVIN_OFFSET
    if temp_k >= 0.0:
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = temp_c >= HIGH_TEMPERATURE_LIMIT_C
        print(f"Fahrenheit: {round(temp_f, DECIMALS)}")
        print(f"Kelvin: {round(temp_k, DECIMALS)}")
        print(f"High temperature: {str(is_high_temperature).lower()}")
    else:
        print(ERROR_MESSAGE)
else:
    print(ERROR_MESSAGE)


# =============================================================================
# Problem 2: Work hours and overtime payment
# =============================================================================
# Description:
#   Calculates the weekly pay of a worker. Up to 40 hours are paid at
#   hourly_rate; hours above 40 are paid at 150% of the rate. It also gives
#   has_overtime, true when the worker did more than 40 hours.
#
# Inputs:
#   - hours_worked (float; hours worked in the week)
#   - hourly_rate (float; pay per hour)
#
# Outputs:
#   - "Regular pay: <regular_pay>"
#   - "Overtime pay: <overtime_pay>"
#   - "Total pay: <total_pay>"
#   - "Has overtime: true|false"
#
# Validations:
#   - hours_worked >= 0
#   - hourly_rate > 0
#   - Otherwise: "Error: invalid input"
#
# Test cases:
#   1) Normal: 45 hours, rate 100 -> regular 4000.0, overtime 750.0,
#      total 4750.0, has overtime true
#   2) Border: 40 hours, rate 100 -> regular 4000.0, overtime 0.0,
#      total 4000.0, has overtime false
#   3) Error:  -5 hours, rate 100 (or rate 0) -> error
print("\n=== Problem 2: Overtime payment ===")
hours_text = input("Enter hours worked: ").strip()
rate_text = input("Enter hourly rate: ").strip()

numeric_texts = [hours_text, rate_text]
max_dots_list = [1, 1]
all_numbers = True
for position in range(len(numeric_texts)):
    text = numeric_texts[position]
    dot_count = 0
    digit_count = 0
    for index in range(len(text)):
        character = text[index]
        if character in DIGITS:
            digit_count += 1
        elif character == ".":
            dot_count += 1
        elif character != "-" or index != 0:
            all_numbers = False
    if digit_count == 0 or dot_count > max_dots_list[position]:
        all_numbers = False

if all_numbers:
    hours_worked = float(hours_text)
    hourly_rate = float(rate_text)
    if hours_worked >= 0 and hourly_rate > 0:
        regular_hours = min(hours_worked, REGULAR_HOURS_LIMIT)
        overtime_hours = max(hours_worked - REGULAR_HOURS_LIMIT, 0.0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > REGULAR_HOURS_LIMIT

        print(f"Regular pay: {round(regular_pay, DECIMALS)}")
        print(f"Overtime pay: {round(overtime_pay, DECIMALS)}")
        print(f"Total pay: {round(total_pay, DECIMALS)}")
        print(f"Has overtime: {str(has_overtime).lower()}")
    else:
        print(ERROR_MESSAGE)
else:
    print(ERROR_MESSAGE)


# =============================================================================
# Problem 3: Discount eligibility with booleans
# =============================================================================
# Description:
#   A customer gets a 10% discount if is_student is true OR is_senior is true
#   OR purchase_total >= 1000.0. The program shows the eligibility and the
#   final total to pay.
#
# Inputs:
#   - purchase_total (float; total of the purchase)
#   - is_student_text (string; "YES" or "NO")
#   - is_senior_text (string; "YES" or "NO")
#
# Outputs:
#   - "Discount eligible: true|false"
#   - "Final total: <final_total>"
#
# Validations:
#   - purchase_total >= 0.0
#   - The texts are normalized (strip + upper) and must be "YES" or "NO".
#   - Otherwise: "Error: invalid input"
#
# Test cases:
#   1) Normal: 500, "yes", "no" -> eligible true, final total 450.0
#   2) Border: 1000.0, "NO", "NO" -> eligible true (exactly 1000), final 900.0
#   3) Error:  500, "maybe", "NO" (or total -10) -> error
print("\n=== Problem 3: Discount eligibility ===")
purchase_text = input("Enter purchase total: ").strip()
is_student_text = input("Is the customer a student? (YES/NO): ").strip().upper()
is_senior_text = input("Is the customer a senior? (YES/NO): ").strip().upper()

numeric_texts = [purchase_text]
max_dots_list = [1]
all_numbers = True
for position in range(len(numeric_texts)):
    text = numeric_texts[position]
    dot_count = 0
    digit_count = 0
    for index in range(len(text)):
        character = text[index]
        if character in DIGITS:
            digit_count += 1
        elif character == ".":
            dot_count += 1
        elif character != "-" or index != 0:
            all_numbers = False
    if digit_count == 0 or dot_count > max_dots_list[position]:
        all_numbers = False

if all_numbers:
    purchase_total = float(purchase_text)
    answers_are_valid = (
        is_student_text in VALID_ANSWERS and is_senior_text in VALID_ANSWERS
    )
    if purchase_total >= 0.0 and answers_are_valid:
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        discount_eligible = (
            is_student or is_senior or (purchase_total >= DISCOUNT_MIN_PURCHASE)
        )
        if discount_eligible:
            final_total = purchase_total * (1 - DISCOUNT_RATE)
        else:
            final_total = purchase_total

        print(f"Discount eligible: {str(discount_eligible).lower()}")
        print(f"Final total: {round(final_total, DECIMALS)}")
    else:
        print(ERROR_MESSAGE)
else:
    print(ERROR_MESSAGE)


# =============================================================================
# Problem 4: Basic statistics of three integers
# =============================================================================
# Description:
#   Reads three integers and calculates the sum, the average (float), the
#   maximum, the minimum and all_even, true when the three numbers are even.
#
# Inputs:
#   - n1, n2, n3 (int)
#
# Outputs:
#   - "Sum: <sum_value>"
#   - "Average: <average_value>"
#   - "Max: <max_value>"
#   - "Min: <min_value>"
#   - "All even: true|false"
#
# Validations:
#   - The three values can be converted to int (negatives are allowed).
#
# Test cases:
#   1) Normal: 4, 7, 10 -> sum 21, average 7.0, max 10, min 4, all even false
#   2) Border: -2, 0, 8 (negative and zero) -> sum 6, average 2.0, max 8,
#      min -2, all even true
#   3) Error:  "3.5", 2, 1 (not an int) or "x" -> error
print("\n=== Problem 4: Statistics of three integers ===")
n1_text = input("Enter the first integer: ").strip()
n2_text = input("Enter the second integer: ").strip()
n3_text = input("Enter the third integer: ").strip()

numeric_texts = [n1_text, n2_text, n3_text]
max_dots_list = [0, 0, 0]  # integers: no decimal point allowed
all_numbers = True
for position in range(len(numeric_texts)):
    text = numeric_texts[position]
    dot_count = 0
    digit_count = 0
    for index in range(len(text)):
        character = text[index]
        if character in DIGITS:
            digit_count += 1
        elif character == ".":
            dot_count += 1
        elif character != "-" or index != 0:
            all_numbers = False
    if digit_count == 0 or dot_count > max_dots_list[position]:
        all_numbers = False

if all_numbers:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)

    numbers = [n1, n2]
    numbers.append(n3)
    sum_value = n1 + n2 + n3
    average_value = sum_value / len(numbers)
    max_value = max(numbers)
    min_value = min(numbers)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, DECIMALS)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")
else:
    print(ERROR_MESSAGE)


# =============================================================================
# Problem 5: Loan eligibility (income and debt ratio)
# =============================================================================
# Description:
#   Decides if a person is eligible for a loan using monthly_income,
#   monthly_debt and credit_score.
#   debt_ratio = monthly_debt / monthly_income
#   eligible is true when monthly_income >= 8000.0 AND debt_ratio <= 0.4
#   AND credit_score >= 650.
#
# Inputs:
#   - monthly_income (float)
#   - monthly_debt (float)
#   - credit_score (int)
#
# Outputs:
#   - "Debt ratio: <debt_ratio>"
#   - "Eligible: true|false"
#
# Validations:
#   - monthly_income > 0.0 (avoids division by zero)
#   - monthly_debt >= 0.0
#   - credit_score >= 0
#   - Otherwise: "Error: invalid input"
#
# Test cases:
#   1) Normal: income 15000, debt 4000, score 700 -> ratio 0.27, eligible true
#   2) Border: income 8000, debt 3200, score 650 -> ratio 0.4, eligible true
#      (all three limits are met exactly)
#   3) Error:  income 0, debt 100, score 700 -> error (division by zero)
print("\n=== Problem 5: Loan eligibility ===")
income_text = input("Enter monthly income: ").strip()
debt_text = input("Enter monthly debt payments: ").strip()
score_text = input("Enter credit score: ").strip()

numeric_texts = [income_text, debt_text, score_text]
max_dots_list = [1, 1, 0]  # the credit score must be an integer
all_numbers = True
for position in range(len(numeric_texts)):
    text = numeric_texts[position]
    dot_count = 0
    digit_count = 0
    for index in range(len(text)):
        character = text[index]
        if character in DIGITS:
            digit_count += 1
        elif character == ".":
            dot_count += 1
        elif character != "-" or index != 0:
            all_numbers = False
    if digit_count == 0 or dot_count > max_dots_list[position]:
        all_numbers = False

if all_numbers:
    monthly_income = float(income_text)
    monthly_debt = float(debt_text)
    credit_score = int(score_text)

    if monthly_income > 0.0 and monthly_debt >= 0.0 and credit_score >= 0:
        debt_ratio = monthly_debt / monthly_income

        failed_rules = []  # one entry per rule that is not met
        if monthly_income < MIN_LOAN_INCOME:
            failed_rules.append("income")
        if debt_ratio > MAX_DEBT_RATIO:
            failed_rules.append("debt ratio")
        if credit_score < MIN_CREDIT_SCORE:
            failed_rules.append("credit score")
        eligible = len(failed_rules) == 0  # same as: rule1 and rule2 and rule3

        print(f"Debt ratio: {round(debt_ratio, DECIMALS)}")
        print(f"Eligible: {str(eligible).lower()}")
    else:
        print(ERROR_MESSAGE)
else:
    print(ERROR_MESSAGE)


# =============================================================================
# Problem 6: Body Mass Index (BMI) and category flag
# =============================================================================
# Description:
#   Calculates bmi = weight_kg / (height_m * height_m) and gives three
#   booleans: is_underweight (bmi < 18.5), is_normal (18.5 <= bmi < 25.0) and
#   is_overweight (bmi >= 25.0). The comparisons use the exact bmi; only the
#   displayed value is rounded to 2 decimals.
#
# Inputs:
#   - weight_kg (float)
#   - height_m (float)
#
# Outputs:
#   - "BMI: <rounded_bmi>"
#   - "Underweight: true|false"
#   - "Normal: true|false"
#   - "Overweight: true|false"
#
# Validations:
#   - weight_kg > 0.0
#   - height_m > 0.0
#   - Otherwise: "Error: invalid input"
#
# Test cases:
#   1) Normal: 70 kg, 1.75 m -> BMI 22.86, normal true
#   2) Border: 100 kg, 2.0 m -> BMI 25.0, overweight true (exact limit)
#   3) Error:  70 kg, 0 m (or weight -5) -> error
print("\n=== Problem 6: BMI ===")
weight_text = input("Enter weight in kg: ").strip()
height_text = input("Enter height in meters: ").strip()

numeric_texts = [weight_text, height_text]
max_dots_list = [1, 1]
all_numbers = True
for position in range(len(numeric_texts)):
    text = numeric_texts[position]
    dot_count = 0
    digit_count = 0
    for index in range(len(text)):
        character = text[index]
        if character in DIGITS:
            digit_count += 1
        elif character == ".":
            dot_count += 1
        elif character != "-" or index != 0:
            all_numbers = False
    if digit_count == 0 or dot_count > max_dots_list[position]:
        all_numbers = False

if all_numbers:
    weight_kg = float(weight_text)
    height_m = float(height_text)
    if weight_kg > 0.0 and height_m > 0.0:
        bmi = weight_kg / (height_m * height_m)
        is_underweight = bmi < UNDERWEIGHT_LIMIT
        is_normal = UNDERWEIGHT_LIMIT <= bmi < OVERWEIGHT_LIMIT
        is_overweight = bmi >= OVERWEIGHT_LIMIT

        print(f"BMI: {round(bmi, DECIMALS)}")
        print(f"Underweight: {str(is_underweight).lower()}")
        print(f"Normal: {str(is_normal).lower()}")
        print(f"Overweight: {str(is_overweight).lower()}")
    else:
        print(ERROR_MESSAGE)
else:
    print(ERROR_MESSAGE)


# =============================================================================
# CONCLUSIONS
# =============================================================================
# Integers and floats work together in real calculations: hours and scores are
# often int or float, while money, ratios and BMI need float for decimals.
# Comparisons such as >=, < or == produce booleans, and those booleans drive
# the if statements that make decisions in the program.
# Validating ranges and avoiding division by zero prevents crashes and wrong
# results, for example with monthly_income = 0 or height_m = 0.
# I learned that combining conditions with and, or and not requires thinking
# about each rule separately: and needs every rule to pass, or needs only one.
# These same patterns repeat in payroll, discounts, loans and health
# calculators, so the same structure (validate, calculate, decide) is reused.

# =============================================================================
# REFERENCES
# =============================================================================
# 1) Python documentation - Built-in Types: Numeric Types - int, float, complex
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2) Python documentation - Boolean Type - bool
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 3) Python Tutorial - An Informal Introduction to Python (Numbers)
#    https://docs.python.org/3/tutorial/introduction.html
# 4) Real Python - Operators and Expressions in Python
#    https://realpython.com/python-operators-expressions/
# 5) Downey, A. - Think Python (Variables, expressions and conditionals),
#    Green Tea Press, https://allendowney.github.io/ThinkPython/
