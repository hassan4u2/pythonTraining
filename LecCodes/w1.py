'''
Write a program that creates a List of ordered numbers from 0 to 9 that does the following:
L = 10, 1, 2, 3, 4, 5, 6, 7, 8, 91
a) Use a slice to create a new List made up of only the even numbers in the List.
b) Use a slice to create a new List made up of only the odd numbers in the List.
c) Print both new Lists.
d) Create a new List that is made up of the 5 even numbers followed by the 5 odd numbers and print the new List.
e) Delete every even-numbered index in the new List and print the new List.
f) Add the element 10 to the List and print the new List.
g) Print the new List after sorting it.
h) Print the new List after reverse sorting it.
Create a new List made up of the first element from the last List repeated 5 times and print this List.
'''


# create a list of numbers from 0 to 9
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1
even = L[0::2]
# 2
odd = L[1::2]
# 3
print(even, odd)
# 4
new = even + odd
# 5
del new[::2]
# 6
new.append(10)
# 7
new.sort()
# 8

