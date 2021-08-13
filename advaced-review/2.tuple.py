# A tuple is a collection of objects which is ordered and immutable(unchangeable).
# https://www.python-engineer.com/courses/advancedpython/02-tuples/

# So similar to list but elements are protected

mytuple = ('a', 'p', 'p', 'l', 'e') #create a tuple
print(mytuple)

# number of elements
print(len(mytuple))

# number of x element
print(mytuple.count('p'))

# index of first item that equal to x
print(mytuple.index('p'))

# repetition
yourtuple = ('a', 'b') * 5
print('Your tuple is :', yourtuple)

# concatenation
ourtuple = mytuple + yourtuple
print('Our tuple is: ', ourtuple)

# convert list to tuple
mylist = ['a', 'b', 'c', 'd']
list2tuple = tuple(mylist)
print('Converted list to tuple: ', list2tuple)

# convert string to tuple
str2tuple = tuple("Hello")
print('Converted string to tuple: ', str2tuple)

# unpacke tuple
myinfo = ('Theara', 25, 'Mechatronics Engineer')
name, age, job = myinfo
print('Name: ', name, ' age: ', age, ' and job: ', job)