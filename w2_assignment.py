# Week Two Assignment
# Submit a github repo link for the assignment below
# Create an empty list called my_list.
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("List created:", my_list)

# Insert the value 15 at the second position in the list.
my_list.insert(1, 15)
print("Value inserted:", my_list)

# Extend my_list with another list: [50, 60, 70].
extended_list = [50, 60, 70]
my_list.extend(extended_list)
print("Extended List added:", my_list)

# Remove the last element from my_list.
removed_element = my_list.pop()
print("Element removed:", removed_element)
print("Updated List:", my_list)

# Sort my_list in ascending order.
my_list.sort()
print("Sorted List:", my_list)

# Find and print the index of the value 30 in my_list.
index_30 = my_list.index(30)
print("Index of 30:", index_30)
