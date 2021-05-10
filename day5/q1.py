# Implement a function that accepts any number or args and kwargs and print those args on a line with space 
# in between and kwargs on another line with space in between.

def func(*args, **kwargs):
    for i in args:
        print(i, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()


func('hello','good morning', fname="arya", lname="jayan")

