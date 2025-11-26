"""
While Loop in Python
Repeats a block of code as long as a condition is True
"""

# 1. Basic while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# 2. While loop with break
i = 1
while True:
    print(i)
    if i == 5: break
    i += 1

# 3. While loop with continue
i = 0
while i < 5:
    i += 1
    if i == 3: continue  # skip number 3
    print(i)

# 4. While loop with else
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop ended")

# 5. Infinite loop (needs break to stop)
while True:
    print("Running...")
    break  # prevents infinite loop
