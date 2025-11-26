"""
Decision Making in Python
Decision making helps programs choose actions based on conditions.
Python uses:
    1. if
    2. if...else
    3. if...elif...else
    4. Nested if
    5. Short Hand if
    6. Short Hand if...else (Ternary)
    7. Logical Operators (and, or, not)
"""

# 1. if statement
age = 18
if age >= 18:
    print("You are eligible to vote.")


# 2. if...else statement
num = 5
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# 3. if...elif...else statement
marks = 72
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# 4. Nested if
age = 20
citizen = True
if age >= 18:
    if citizen:
        print("You can vote in this country.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You are not old enough to vote.")


# 5. Short Hand if
x = 10
if x > 5: print("x is greater than 5")


# 6. Short Hand if...else (Ternary Operator)
a = 5
b = 10
result = "A is greater" if a > b else "B is greater"
print(result)


# 7. Combining Conditions using and, or, not
age = 25
has_id = True
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

is_active = False
if not is_active:
    print("Account is inactive")


# Practice Example
temperature = 35
if temperature > 30:
    print("It’s a hot day.")
elif temperature > 20:
    print("Nice weather.")
else:
    print("It's cold.")
