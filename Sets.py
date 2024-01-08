# Creating a set
numbers_set = {3, 1, 4, 1, 5, 9, 2, 6, 5}

# Displaying the set
print("Original Set:", numbers_set)

# Adding an element to the set
numbers_set.add(7)
print("After Adding 7:", numbers_set)

# Removing an element from the set
numbers_set.remove(5)
print("After Removing 5:", numbers_set)

# Checking if an element exists in the set
contains_9 = 9 in numbers_set
print("Contains 9:", contains_9)

# Checking the length of the set
length = len(numbers_set)
print("Length of Set:", length)

# Creating another set
more_numbers = {4, 6, 8, 10}

# Union of two sets
union_set = numbers_set.union(more_numbers)
print("Union Set:", union_set)

# Intersection of two sets
intersection_set = numbers_set.intersection(more_numbers)
print("Intersection Set:", intersection_set)

# Difference between two sets
difference_set = numbers_set.difference(more_numbers)
print("Difference Set (numbers_set - more_numbers):", difference_set)

# Adding elements from another set
numbers_set.update({6, 7})
print("After Updating Set 1:", numbers_set)
