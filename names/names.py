import time
from binary_search_tree_copy import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# Original runtime: 4.725 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Runtime 0.751 seconds, but i think it's cheating? 
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)

#### MVP ###
# using Binary Search Tree b/c that seems like what we're supposed to do:
# Runtime: 0.084 seconds

# initialize the BST with dummy value
"""
tree = BSTNode("val")

# set name_1 as a BST
for name in names_1:
    tree.insert(name)

# find matches from name_2 in BST
for other_name in names_2:
    if tree.contains(other_name):
        duplicates.append(other_name)
"""

### Stretch ###
# Runtime: 0.004 seconds
duplicates = list(set(names_1)&set(names_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
