""" You will develop your understanding and application of Python programming through this series of exercises. Each question is designed to challenge and enhance your skills in working with Python’s built-in data structures and functions.

 

Question 1  : 

Write a Python program that multiplies all the items in a list.

Sample list= [2, 3, 6]

Result = 36

Question 2

Write a Python program to get a list, sorted in increasing order by the last element in each tuple, from a given list of non-empty tuples.

Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

Expected result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

Hint: You can use the sort function.

Question 3 

Write a Python program that combines two dictionaries by adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c':300}

d2 = {'a': 300, 'b': 200, 'd':400}

Expected result: {'a': 400, 'b': 400, 'd': 400, 'c': 300}

Question 4

With a given integral number n, write a program to generate a dictionary that contains (i, i*i) so that is an integral number between 1 and n (both included). Then the program should print the dictionary. Suppose the following input is supplied to the program: 8. Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Question 5

Write a program to sort a tuple by its float element.

For example: list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

Expected result: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

Question 6

Write a Python program to create a set.

Examples : {0, 1, 2, 3, 4}

Write a Python program to iteration over sets.

Write a Python program to add members in a set and to remove items from a given set. """

#Question 01
My_list = []
while True:
    Value = input("Enter a number to add to the list (or type 'done' to finish): ")
    if Value == "done":
        break
    else:
        My_list.append(int(Value))
print(f"Your list: {My_list}")

# Multiply all items in the list
result = 1
for num in My_list:
    result *= num
print(f"The product of all items in the list is: {result}")

#Question 02

List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def Get_last(t):
    return t[-1]

print(sorted(List, key=Get_last)) #print(sorted(List, key=lambda x : x[-1]))   

#Question 03

# Sample dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Final result dictionary
result = {}

# Step 1: Add values for common keys
for key in d1:
    if key in d2:
        result[key] = d1[key] + d2[key]
    else:
        result[key] = d1[key]

# Step 2: Add remaining keys from d2 that weren't in d1
for key in d2:
    if key not in d1:
        result[key] = d2[key]

print(result)

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
# Combine two dictionaries by adding values for common keys
keys = set(list(d1.keys()) + list(d2.keys()))

d3 = {}
for key in keys:
    d3[key] = d1.get(key, 0) + d2.get(key, 0)
print(d3)


#Question 04

input_number = int(input("Enter an integral number n: "))
result_dict = {}
for i in range(input_number + 1):
    result_dict[i] = i*i
print(result_dict)


#Question 05


list_ = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

def get_float(t):
    return float(t[1])

# Sort in descending order by the float value
print(sorted(list_, key=get_float, reverse=True))

#Question 06

# Create a set with numbers from 0 to 4
my_set = {0, 1, 2, 3, 4}
print(my_set)

# Add elements
my_set.add(6)
my_set.add(5)

for item in my_set:
    print(item)
    
# Remove elements
my_set.remove(2)     # Raises error if item doesn't exist
my_set.discard(10)   # Safe: no error even if item isn't in set

print(my_set)