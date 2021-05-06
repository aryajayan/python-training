# write an add function that returns some of two numbers. Accept an optional third parameter that can make it print the output too

def get_sum(num1, num2, opt=False):
    sum=num1+num2
    if opt:
        print("sum in function = ", sum)
    return sum

print(get_sum(3,4))
get_sum(3,4,True)

# --Output--
# 7
# sum in function =  7