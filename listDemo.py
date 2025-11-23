"""
What is List?
A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.

Lists are just like dynamic sized arrays, similar to vector in C++ and ArrayList in Java.

Lists need not be homogeneous always which makes it a most powerful tool in Python. This means a single list may contain DataTypes like Integers, Strings, as well as Objects. In other words a list can contain different types of elements.


"""

# Define a list
list1 = ["a","b","c","d"]

# print the list

print(list)


#  Access the element of list

print(list1[3])

# total no. of  elements in a list

print(len(list1))

# Replace an element from list

list1[3] = "f"
print(list1)


#  find the index no. of an element

x = list1.index("c")
print(x)

# Append an element in list 
list1.append("G")
print(list1)

# insert an element on a specific index no.
list1.insert(2,"h")
print(list1)

# Loop with the list

for x in list1:      # for(int i=0; i<10; i++) 
    print(x)    
    

# Check if the lement exists or not

if "a" in list1:
    print("yes, a is present")

