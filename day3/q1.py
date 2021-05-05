# Given a list of names, try printing unique names that are less than 5 character length and do not contain the character 'e'

names= ["john", "jake", "jack", "george", "jenny", "jason"]
for a in set(names):
    if len(a) < 5:
        if 'e' not in a:
            print(a)

# --Output--
# jack
# john
