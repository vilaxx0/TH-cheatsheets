# DataTyes
    # str	                        Text
    # int, float, complex       	Numeric
    # list, tuple, range        	Sequence
    # dict                      	Mapping
    # set, frozenset	            Set
    # bool                      	Boolean
    # bytes, bytearray,         	Binary

# Built-in string methods
'''
capitalize() Converts the first character to upper case
casefold() Converts string into lower case
center() Returns a centered string
count() Returns the number of times a specified value occurs in a string
encode() Returns an encoded version of the string
endswith() Returns true if the string ends with the specified value
expandtabs() Sets the tab size of the string
find() Searches the string for a specified value and returns the position of where it was found
format() Formats specified values in a string
format_map() Formats specified values in a string
index() Searches the string for a specified value and returns the position of where it was found
isalnum() Returns True if all characters in the string are alphanumeric
isalpha() Returns True if all characters in the string are in the alphabet
isascii() Returns True if all characters in the string are ascii characters
isdecimal() Returns True if all characters in the string are decimals
isdigit() Returns True if all characters in the string are digits
isidentifier() Returns True if the string is an identifier
islower() Returns True if all characters in the string are lower case
isnumeric() Returns True if all characters in the string are numeric
isprintable() Returns True if all characters in the string are printable
isspace() Returns True if all characters in the string are whitespaces
istitle() Returns True if the string follows the rules of a title
isupper() Returns True if all characters in the string are upper case
join() Converts the elements of an iterable into a string
ljust() Returns a left justified version of the string
lower() Converts a string into lower case
lstrip() Returns a left trim version of the string
maketrans() Returns a translation table to be used in translations
partition() Returns a tuple where the string is parted into three parts
replace() Returns a string where a specified value is replaced with a specified value
rfind()	 Searches the string for a specified value and returns the last position of where it was found
rindex() Searches the string for a specified value and returns the last position of where it was found
rjust() Returns a right justified version of the string
rpartition() Returns a tuple where the string is parted into three parts
rsplit() Splits the string at the specified separator, and returns a list
rstrip() Returns a right trim version of the string
split() Splits the string at the specified separator, and returns a list
splitlines() Splits the string at line breaks and returns a list
startswith() Returns true if the string starts with the specified value
strip() Returns a trimmed version of the string
swapcase() Swaps cases, lower case becomes upper case and vice versa
title() Converts the first character of each word to upper case
translate() Returns a translated string
upper() Converts a string into upper case
zfill() Fills the string with a specified number of 0 values at the beginning
'''
# Variables
age = 18      # age is of type int
name = "John" # name is now of type str

# Collections
    # Simple array
squares = [1, 4, 9, 16, 25]
    #Length
len(squares)

    #built-in function list()
x = list(('bobby', 'at', 'didcoding','dot', 'com')) # creates a list object
x.append(1)

    # Dictionary
some_dict = {
    'a_key': 'a_value',
    'a_key_2': 'a_value_2',
    'a_key_3': ['a_list', 'as', 'a value'],
    'a_key_4': {'a_dict': 'as a value'}
}

# Conditional Statements
    # If else
def number_play(x):
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

# Loops
    # For
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

    # Match (like switch in C#)
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# Functions
def demo_func(param:int):
    calc = param + 4
    return calc
# Classes & Objects
class MyClass:
    def __init__(self, my_int:int):
        self.i = my_int
    
    def f(self):
        new = self.i ** 3
        return new

# Exceptions
try:
    result = x / y
    print("THIS IS TRY")
except ZeroDivisionError:
    print("division by zero!")
except TypeError:
    print("Must be int!")
else:
    print("result is", result)
finally:
    print("executing finally clause")
