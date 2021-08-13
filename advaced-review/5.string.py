# https://www.python-engineer.com/courses/advancedpython/05-strings/

# create string
str_1 = 'Hello'
str_2 = "I'm a 'Geek'"
print(str_2)

# escaping ackslash
str_3 = 'I\'m a "Geek"'
print(str_3)

# multiline strings
str_4 = '''Hello there,
How are you?
I am good.'''
print(str_4)

# backslash to continue in the next line
str_5 = 'Hello\
    World.'
print(str_5)

# conatenate string
str_a = "Hello"
str_b = ", How are you?"
sentence = str_a + str_b
print(sentence)

# subtstring exits
if "llo" in "Hello":
    print("yes")

# USEFUL METHOD
mystr = "     Hello there, how are you?     "

#remove white space
strip_str = mystr.strip()
print(strip_str)

# lenght of string
print('Lenght of string: ', len(strip_str))

# Upper and lower cases
print(strip_str.upper())
print(strip_str.lower())

# startswith and enswitch
print('Hello'.startswith('He'))
print('Hello'.endswith('llo'))

# find first index of a given substring, -1 otherwise
print('Hello'.find('e'))

# count number of characters
print('Hello'.count('l'))

# replace a substring with another
message = 'Hello World'
new_message = message.replace('World', 'Universe')
print(new_message)

# split the string into a list
my_string = "how are you doing"
a = my_string.split() # default argument is " "
print(a)
my_string = "one,two,three"
a = my_string.split(",")
print(a)

# join elements of a list into a string
my_list = ['How', 'are', 'you', 'doing']
a = ' '.join(my_list) # the given string is the separator, e.g. ' ' between each argument
print(a)