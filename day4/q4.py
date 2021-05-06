# write a product function that produces product of its args. It should accept any number of args

def get_product(*args):
    prod=1
    for n in args:
        prod=prod*n
    return prod

print("product is" , get_product(2,3,1))
print("product is" , get_product(5,6))
print("product is" , get_product())

# --output--
# product is 6
# product is 30
# product is 1