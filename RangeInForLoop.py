"""
Range in For Loop (Python)
Used to generate a sequence of numbers for iteration
Syntax:
range(stop)
range(start, stop)
range(start, stop, step)
"""

# 1. range(stop) – numbers from 0 to stop-1
for i in range(5):  # 0 1 2 3 4
    print(i)

# 2. range(start, stop) – numbers from start to stop-1
for i in range(2, 6):  # 2 3 4 5
    print(i)

# 3. range(start, stop, step) – numbers with step
for i in range(1, 10, 2):  # 1 3 5 7 9
    print(i)

# 4. Using range in reverse
for i in range(5, 0, -1):  # 5 4 3 2 1
    print(i)

# 5. Using range with list indexing
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])
