"""
What is Tuple?
Tuple is another type of collection such as List.
The difference is tuple is written with round brackets.
And it is ordered and unchangeable.
That means once tuple is created you cannot change the values.
This also means once tuple is created you cannot add items to it.
And you cannot remove items from tuple.
But we can delete tuple.
"""

# 1. Defining a tuple
tuple1 = ("A", "B", "C", "D", "E", "F", "G")
print("Tuple:", tuple1)

# 2. Accessing items (indexing)
print("First item:", tuple1[0])
print("Last item:", tuple1[-1])

# 3. Slicing a tuple
print("Slice items (1 to 3):", tuple1[1:4])

# 4. Checking if an item exists
if "D" in tuple1:
    print("Yes, 'D' is in the tuple")

# 5. Length of a tuple
print("Length of tuple:", len(tuple1))

# 6. Converting tuple to list (to modify items)
list1 = list(tuple1)
list1.append("H")  # adding a new value
print("Converted to list and modified:", list1)

# 7. Converting list back to tuple
tuple2 = tuple(list1)
print("Converted back to tuple:", tuple2)

# 8. Counting elements
print("Count of 'A':", tuple2.count("A"))

# 9. Finding index of an item
print("Index of 'C':", tuple2.index("C"))

# 10. Joining two tuples
tuple3 = ("X", "Y", "Z")
tuple4 = tuple1 + tuple3
print("Joined tuple:", tuple4)

# 11. Deleting a tuple completely
del tuple1
# print(tuple1)  # This will show an error because tuple1 is deleted
