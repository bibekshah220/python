"""
For Loop in Python
Used to iterate over sequences (list, string, tuple, range)
"""

# 1. Basic for loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits: print(fruit)

# 2. For loop with string
for letter in "hello": print(letter)

# 3. For loop with range()
for i in range(5): print(i)  # 0 1 2 3 4

# 4. For loop inside a function
def print_numbers(n):
    for i in range(1, n+1): print(i)
print_numbers(5)

# 5. Sum of list using for loop in function
def sum_list(nums):
    total = 0
    for num in nums: total += num
    return total
print(sum_list([10, 20, 30]))  # 60

# 6. Nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# 7. Loop with condition
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0: print(num, "is even")
