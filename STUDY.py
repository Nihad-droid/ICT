"""
print()
variable
str(), int(), float(), bool()       "respectively string, integer, floating point, boolean data type converter"
type()              "returns the type of anything"
True, False, None   "Boolean logics"
variable += 1       "increment"
len()               "length of"
.find()             "finds a substring. -1 if there isn't" .find(substring, start, stop)
.capitalize()       "yusif becomes Yusif
.upper()            "uppercase all"
.lower()
.islower()      "checks whether letters are lowercase or not"
.isupper()
.isdigit()          "Gives a Boolean value whether it's digit or not. Only works with str variables.
                    "Any string with only digits(no other symbol) gives True."
.isalpha()          "gives a Boolean value whether it's only abc letter. Even spaces are not allowed to yield True!!!"
.isalnum()          "gives a boolean whethet only contains alphanumeric and has at least one character"
.startswith(), .endwith()  "name says it all(gives bool)"
.count()                   "variable.count("o") counts how many o letters are there. Only works with strings"
.replace("x","y")          "replaces all "x"s with "y"s. Only strings.
print(variable * x)        "print variable x times"
int(str or float variable) "turns string or float into integer type. Note: decimal point gets truncated."
input()                    "accepts user input"
.rjust(x,y), ljust(x,y)    "used to justify. Look string formatting for further info"
.center(x,y)               "same as rjust and ljust"
.strip(x)                  "strips off characters from both sides, order of characters in string doesnt matter"
.lstrip(x)                 "strip off from left only"
.rstrip(x)                 "strip off from right only"
import pyperclip
    .copy(x)        "copies given data to clipboard"
    .paste()        "pastes your clipboard"

import math
    round() "rounds the number: 3.14 becomes 3. You can add 2nd argument to choose how many digits to round."
    .ceil() "round up to the nearest integer: 3.14 becomes 4"
    .floor() "round down to the nearest integer: 3.14 becomes 3"
    .abs() "absolute value of the number: -3.14 becomes 3.14"
    .pow(x, y) "x to the power of y: x^y can also be written instead"
    .sqrt() "square root of the number: 3.14 becomes 1.612451"
    min() "finds the minimum number among given"
    max() "opposite of min()"
slicing = create a substring by extracting elements from another string
    variable[start:stop:step] (any blank value is accepted as 0)(using negative value for step will reserve)
    slicing_defined_as_a_variable = slice(start:stop:step)
        print(variable[slicing_defined_as_a_variable])
    .join()             "joins items in a list with the given character"
    .split()            "opposite of join, both accepts no argument as a whitespace"
if, elif, else statements (requires colon after conditions except for else)
>, <, <=, >=, !, ==     *note: dont use single equal sign as python will confuse it by variable assignment
and, or, not
in              "it literally means 'in'. Checks whether given list or tuple comprises the given data"
while loop      "while statement makes its code run forever as long as the condition is true"
for loop, range()
    for i in range(x, y, z)  "the code will loop until i becomes y with steps of z just like in slicing"
    "i starts with x itself (if there is nothing, it is 0) and stops at right before y with steps of z"
    "Just like mathematical indentation [x;y)"

import time:
    .sleep()    "suspend execution for given number of seconds"
    .time()     "return current time in seconds since epoch(1970,1 January 00:00:00"
end=""          "used mostly in print() and prevents loops from adding a paragraph space
loop control:
    break       "used to terminate the loop entirely
    continue    "skips to the next iteration of the loop
    pass        "does nothing, acts as a placeholder
list:  [a,b]        "used to store multiple item in a single variable" "ordered and changeable"
    list.append()     "add an item"
    list.remove()     "removes the given item"
    list.pop()        "remove the item of a given index"
    list.insert()     "inserts an item to a given index"
    list.sort()       "sorts the list alphabetically"
        list.sort(reverse=True)   "reverse alphabetical sorting"
        list.sort(key=func)       "by writing an appropriate function, you can define how you want to sort"
    list.clear()      "eradicates all items from the list"
tuple: (a,b)     "collection which is ordered and unchangeable"
    tuple.index()     "finds the index of given item"
    tuple.count()     "finds the number of given item"
    sorted(tuple)     "can be used to sort tuple alphabetically, though it actually makes it list to achieve it"
set:   {a,b}     "collection which is unordered, unindexed. No duplicate values. The brackets are called curly brackets"
                 "when you print it, the elements are ordered randomly each time as there is no order"
    set.add()                    "adds the element"
    set.remove()                 "removes the item"
    set.clear()                  "eradicates all elements"
    set.update(set_2)            "adds all elements of set_2 to the set"
    set = set_2.union(set_3)     "combines set_2 with set_3 to create set. Only one is copied if there are Duplicate."
    set.difference(set_2)        "finds the difference between sets"
    set.intersection(set_2)      "finds the intersection between sets(elements that both include)"
dictionary:  {key: value}   "changeable, unordered collection of key-value pairs"
    dict[key]                               "gives the value of the given key. Error will occur if a key doesnt exist"
    dict.get()                              "gets the key by avoiding KeyError"
    dict.keys()                             "gives all the keys"
    dict.values()                           "gives all the values
    dict.items()                            "returns a view object that displays a list of the dictionary's
                                             key-value pairs as tuples"
    dict.update({new_key: new_value})       "add a new pair to dictionary"
    dict.pop()                              "removes the given key and its value"
    dict.clear()                            "empties the dictionary"
index operators:  []            "works with str,list, tuples only"
    variable[starting:stopping:steps]
function:  def hello(parameters):           "a block of code which is executed only when it is called"
return                          "sends value or objects back to the caller"
keyword arguments               "allows the order of the arguments to not matter, unlike positional arguments.
local global        "local variable is only available inside the region unlike global, which is recognized everywhere"
*args                "its a parameter that will pack all arguments into a tuple"
**kwargs             "its a parameter that will pack all argument into a dictionary"
str.format()         "optional method that gives users more control when displaying output"
    print("The {} jumped over the {}".format(variable1, variable2))
    "You can also add index into the {} to specifically choose which variable you would like"
    {:<10}           "this allocates 10 spaces worth of room for your variable by aligning to the left"
    {:>10}           "this allocates 10 spaces worth of room for your variable by aligning to the right"
    {:^10}           "centers it inside that 10 spaces worth of room"
    {:.2f}           "rounds the number by 2 digits after comma"
    {:,}             "adds commas for easier depiction of thousands: 10000000 becomes 10,000,000"
    {:b}             "displays your number as binary!"
    {:o}             "displays your number as octadecimal (8)"
    {:X}             "displays your number as hexadecimal (16)"
    {:E}             "displays the scientific notation of your number"
import random
    random.randint(x,y)     "generates random integer between x and y"
    random.random()          "random between 0 and 1"
    random.choice(list)     "random choice from a given list"
    random.shuffle(list)    "shuffles a given list"
exception           "events detected during execution that interrupts the flow of program"
    try             "tries the following code"
    except          "do this if the given problem occurs"
    except Error as e:      "allows you to assign the error itself as a variable"
import os
    os.path.exists()        "checks if the path exists"
    os.path.isfile()        "checks if its a file"
    os.path.isdir()         "checks if its a folder(directory)"
.center(rooms)      "centers your text along the given character length room"
with open(filename, mode) as file_object:       "a safe way to handle file operations. It auto closes the file after."
    modes:
        r - read
        w - write
        a - append
        rb and rw for binary datas
file.read()         "Reads file"
file.write(text)    "Writes text into file. Overwrites if already exists"
file.closed         "Gives boolean value as to whether file is closed"
import shutil
    shutil.copyfile(source, destination)      "copies contents of a file"
    shutil.copy()                             "copyfile() + permission mode + destination can be a directory"
    shutil.copy2()                            "copy() + copies metadata
import os
    os.replace(source, destination)           "replaces the files"
    os.remove(path)                           "deletes the file"
    os.rmdir(path)                            "deletes the directory. This pathetic command can only delete empty dirs!"
import shutil
    shutil.rmtree(path)                       "DANGEROUS. Deletes folder with all files within it permanently!
modules                                       "files containing python code"
    from {module name} import {function}      "eliminates the need of writing module.function() each time.
    from {module name} import *               "all functions. Not recommended as it can contradict with other modules"
    help("modules")                           "prints the complete list of modules"

OBJECT ORIENTED PROGRAMMING         "Object-oriented programming is a way of structuring code around
                                    "objects — bundles of data (attributes) and functions (methods)."
    class ClassName:                    "This is how you create a class"
        def __init__(self, args):       "__init__ is used to initiate the creation of your object"
        self.attribute = value          "self argument must always be present and it represents the object itself"

        def method():                   "the functions build inside the class are called methods"
            ...
    from ModuleName import ClassName    "Use this to import a class from another python file"



    class Demo:
        x = 10      # class variable            "class variable is the default variable for all object within the class"
                                                "declaring other x will overwrite your default x"
    def __init__(self, y):
        self.y = y    # instance variable
                                                "An instance variable is a variable that belongs to a
                                                 specific object created from a class"


    class Animal:                                "Inheritance is a hierarchy of classes"
        alive = True                             "Child can inherit its parent class"
    class Dog(Animal):
        pass                                     "But if the child class has the same method as parent, it will
    class Cat(Animal):                           "overwrite the mother's method" - method overwriting
        pass


    super functions:
        super().__init__(args)             "function used to give access to methods of a parent class"
                                           "returns a temporary object of a parent class when used"

    abstract methods:                      "prevents a user from creating an object of that class"
        @abstractmethod:                   "a method that has declaration but doesnt have an implementation"
        def method(self):                  "a class containing abstract methods are called abstract class"
            print("")


    objects as arguments:                  "You can add objects as arguments into functions"
        def function(object, color)
            object.color = color


    duck typing:
        class Person():
            def catch(self, duck):          "use the methods inside the duck class without checking if they exist"
                duck.walk()                 "No inheritance, no promises in advance, no class checks"
                duck.talk()                 "If it looks like a duck and quacks like a duck, it is treated as a duck."
                print("You caught it!")

walrus operator:
    while (food := input("what do you want? ")) != "quit":      "declare a variable in the middle of an expression"

import re
    .compile()                      "compile a regex pattern object"
    variable.search()               "seach the data once it fits the pattern"
    variable.findall()              "search for all pattern matches"
    .group()                        "used to retrieve the text that was matched by the regex"

higher order functions
    "a function can be argument or return value of another function too!"

lambda function:                    "function written in 1 line using lambda keyword"
    double = lambda x:x * 2         "accepts any number of atguments, but only has one expression
    print(double(5))                "useful if you need a short, temporary operation"

    restriction = lambda age:True if age>=18 else False     "just another example demonstrating conditionals"

map(func,iterable)                   "map function applies a function to each item in an iterable(list, tuple, etc.)"
filter(func, iterable)               "it is obvious by its name"
return(func, iterable)               "reduce it to a single cumulative value by applying a function"

list comprehension:                          "a way to create lists with less syntax. Its similar to lambda function"
    squares = [i * i for i in range(1,11)]   "instead of creating a for loop in separate lines, do this"
    print(squares)

"""
import pyperclip, math, shutil, os, time, random, re, functools
