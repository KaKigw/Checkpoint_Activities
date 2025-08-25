#Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def distinct_numbers(numbers):
    if len(numbers) == len(set(numbers)):
        return True
    else:
        return False
x = [2,3,4,4,32,2]
y = [3,2,5,8,0]
print(distinct_numbers(x))
print(distinct_numbers(y))

