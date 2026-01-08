# Task 1: The append() Method(feat.len)

my_list = ["apple", "bannana", "cherry"]
print(len(my_list))
user_item = input("Enter a new item: ")
my_list.append(user_item)
print((len(my_list)))



# Task 2: The insert() Method

my_list = ["apple", "banna", "cherry", "date"]
my_list.insert(1, "orange")
print(my_list)


# Task 3: Concatenation (+) and Replication(*)

row = ['_'] * 3
add_on = ['X', 'O']
final_row = row + add_on
print(final_row)


# Task 4: THe extend() Method

backpack = ['book', 'pen']
found_items = ['apple', 'map']
print("Before extend:")
print("Backpack:", backpack)
print("Found items:", found_items)
print("\nAfter extend:")
print("Backpack:", backpack)


# Task 5: THe remove() Method (feat.count()

numbers = [1, 5, 5, 5, 9]
print("Count before remove:", numbers.count(5))
numbers.remove(5)
print("Count after remove:", numbers.count(5))


# Task 6: The pop() Method

vip_list = ["Alice", "Bob", "Charlie", "Diana"]
kicked_out = vip_list.pop(0)
print(f"We removed {kicked_out} from the party.")
print(vip_list)


# Task 7: The del Statement (slicing)

numbers = list(range(1, 11))
del numbers[3:6]
print(numbers)


# Task 8: The index() Method (feat.in)

items = ["keys", "wallet", "phone", "charger"]
search_item = input("Type an item to find: ")
if search_item in items:
    print("Item found at index:", items.index(search_item))
else:
    print("Safe! That item is not in the list.")


# Task 9: Ordering (sort and reverse)

numbers = [42, 7, 19, 3, 28]
numbers.sort()
print("Sorted (low to high):", numbers)
numbers.reverse()
print("Reversed (high to low):", numbers)

# Task 10: The copy() Method

original = [1, 2, 3]
backup = original.copy()
original.clear()
print("Backup:", backup)

# Task 11:Random Selection (random.choice)

import random
answers = ["Yes", "No", "Maybe", "Ask again later", "Definitely"]
print(random.choice(answers))
print(random.choice(answers))
print(random.choice(answers))


# Task 12: Nested Lists (Accessing 2D data)

matrix = [[1, 2], [3, 4]]
print(matrix[1][0])
