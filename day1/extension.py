# Given any file python file (like something.py) use slicing to
# print the extension alone (py - don't include .)
# print the file name (something)

str="python.py"
ext=str[-2:]
print(ext)

filename=str[:-3]
print(filename)