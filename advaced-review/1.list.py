# List is a collection data type which is ordered and mutable
# https://www.python-engineer.com/courses/advancedpython/01-lists/

# create empty list
ls_1 = list()
print(ls_1)

# create list with data
ls_2 = ["Theara", 25, True, 2021]
#item       0      1    2     3
#revers    -4     -3   -2    -1
print(ls_2)
print("He is ", ls_2[1])
print("He is ", ls_2[-3])

#useful method
mylist = ['Theara', 25, "single", 2021, True, "Engineer"]

# number of elements
print("my list has ", len(mylist), " elements.")

# adds an element at the end of the list
mylist.append("Kampot")
print('The end of the list is: ',mylist[-1])

# add an elemnt to specific location
mylist.insert(2, "Unknow")
print(mylist)

# removes and returns the item at the given position, default is the last item
popitemlast = mylist.pop()
popitemsecond = mylist.pop(2)
print('Popped last item: ', popitemlast)
print('Popped secon item: ', popitemsecond)
print(mylist) # check list again after remove

# remove item from list
mylist.remove('single')
print('After remove single: ', mylist)

# clear all items in list
copylist = mylist.copy()   # coppy to another list
copylist.clear()
print(copylist)

# reverse item
mylist.reverse()
print(mylist)

# sort items in ascending order, need to be same type of data
fruit = ['banana', 'apple', 'cherry']
fruit.sort()
print('Shorted: ', fruit)

# sort list and past to new list, keep original
fruit_2 = ['banana', 'apple', 'cherry']
copy_fruit = sorted(fruit_2)
print('fruit_2: ', fruit_2)
print('copy_fruit: ',copy_fruit)

# create list with repeat elements
zero_list = [0] * 5
print(zero_list)

# adds element from one list to another, concatenation
list_concat = fruit_2 + zero_list
print(list_concat)

# string to list, char array
string2list = list('Hello')
print(string2list)

# Access sub parts of the list wih the use of colon (:), just as with strings.
# a[start:stop:step], default step is 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
a[0:3] = [0] # replace sub-parts, you need an iterable here
print(a)
b = a[::2] # start to end with every second item
print(b)
a = a[::-1] # reverse the list with a negative step:
print(a)
b = a[:] # copy a list with slicing
print(b)