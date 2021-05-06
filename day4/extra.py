def do_print(*args, seperator=' ', endchar="\n"): #("hello","arya")
    for a in args:
        if a==args[-1]:
            print(a,end="")
        else:
            print(a, end=seperator)
    print(end=endchar)

do_print("hello","arya")
do_print("hi", "heloo", seperator="-")
do_print("howdy",endchar=" ")
do_print("good",endchar=" ")
print()

# --Output--
# hello arya
# hi-heloo
# howdy good


def do_sum(*args, starts_with=0):
    if not all(isinstance(v, int) for v in args) or not isinstance(starts_with, int):
        raise TypeError("'str' object cannot be interpreted as an integer")
    sum=starts_with
    for i in args:
        sum+=i
    return sum

print(do_sum(5,6,7))
print(do_sum(10,20, starts_with=5))
print(do_sum(5,6,"test"))


# --Output--
# 18
# 35

#   File "C:\Users\aryak\learning\python\python-training\day4\extra.py", line 29, in <module>
#     print(do_sum(5,6,"test"))
#   File "C:\Users\aryak\learning\python\python-training\day4\extra.py", line 23, in do_sum
#     raise TypeError("'str' object cannot be interpreted as an integer")
# TypeError: 'str' object cannot be interpreted as an integer


def set_range(*args):
    rlist=[]
    start=0
    stop=None
    step=1
    
    if len(args)==0:
        raise TypeError("range expected at least 1 argument")
    if len(args)>3:
        raise TypeError(f"range expected at most 3 arguments, got {len(args)}")
    if not all(isinstance(v, int) for v in args):
        raise TypeError("'str' object cannot be interpreted as an integer")
    if len(args)==1:
        stop=args[0]
    elif len(args)==2 or len(args)==3:
        start=args[0]
        stop=args[1]
        if len(args)==3:
            step=args[2]
      
    while(start<stop):
        rlist.append(start)
        start+=step
    return rlist

print(set_range(5))
print(set_range(3,10))
print(set_range())
print(set_range(2,4,5,6,7))
print(set_range(4,20,"test"))


# --Output--
# [0, 1, 2, 3, 4]
# [3, 4, 5, 6, 7, 8, 9]

#   File "C:\Users\aryak\learning\python\python-training\day4\extra.py", line 58, in <module>
#     print(set_range(2,4,5,6,7))
#   File "C:\Users\aryak\learning\python\python-training\day4\extra.py", line 39, in set_range
#     raise TypeError(f"range expected at most 3 arguments, got {len(args)}")
# TypeError: range expected at most 3 arguments, got 5

#   File "C:\Users\aryak\learning\python\python-training\day4\extra.py", line 58, in <module>
#     print(set_range(2,4,5,6,7))
#   File "C:\Users\aryak\learning\python\python-training\day4\extra.py", line 39, in set_range
#     raise TypeError(f"range expected at most 3 arguments, got {len(args)}")
# TypeError: range expected at most 3 arguments, got 5

# Traceback (most recent call last):
#   File "C:\Users\aryak\learning\python\python-training\day4\extra.py", line 59, in <module>
#     print(set_range(4,20,"test"))
#   File "C:\Users\aryak\learning\python\python-training\day4\extra.py", line 41, in set_range
#     raise TypeError("'str' object cannot be interpreted as an integer")
# TypeError: 'str' object cannot be interpreted as an integer