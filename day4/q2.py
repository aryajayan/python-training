# write a function that accepts N and prints 5 multiples of N
# get_multiple(5) should print 5 10 15 20 25. you'll have to work with range and 
# a bit of custom logic to figure out the stop value.In case of get_multiples(3), 
# output should be 3 6 9 12 15. N can be any positive int. not just 3 or 5.

def get_multiples(n):
    for i in range(n,n*6, n):
        print(i, end=" ")
    print()

num=int(input("Enter the number : "))
get_multiples(num)
# --output--
# Enter the number : 5
# 5 10 15 20 25 