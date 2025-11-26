"""
Remove Item
There are several methods to remove items from list:
1. remove()        - Removes specific item.
2. pop(indexNo)    - Removes the specified index.
3. pop()           - Removes the last item if index is not specified.
4. del keyword     - del keyword with given index number deletes specific element.
5. del keyword     - del keyword without index number deletes whole list.
6. clear()         - Empties the list, will not delete the list.
"""

# Define a list
list1 = ["A", "B", "C", "D", "E"]
list2 = ["1", "2", "3", "4", "5"]

print(list1)

# using remove()
list1.remove("C")
print(list1)

# uising pop() with index no.
list1.pop(1)
print(list1)


# uising pop() without index no.
list1.pop()
print(list1)


#  using del keywords with index no.
del list2[3]
print(list2)

#  using del keywords without index no.
del list2      #delete whole list2
print(list2)

#using clear ()
list1.clear()
print(list1)
