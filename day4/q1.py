# else
# write a loop with an else clause being invoked
# now modify the program so the else clause doesn't run

characters=['b','c','d','f','g','h']

for c in characters:
    if c in ('a','e','i','o','u'):
        print("vowel found - " + c)
        break
    print(c)
else:
    print('vowel not found !')
    
characters=['b','c','i','f','g','h']

for c in characters:
    if c in ('a','e','i','o','u'):
        print("vowel found - " + c)
        break
    print(c)
else:
    print('vowel not found !')


# --Output--
# b
# c
# d
# f
# g
# h
# vowel not found !
# b
# c
# vowel found - i