# Guessing Game. Accept a guess number and tell us if it's higher or less than the hardcoded number

num=10

guess_num=int(input("Guess the number : "))

if guess_num>num:
    print("higher than the given number")
elif guess_num<num:
    print("lower than the given number")
else:
    print("You got the number")


# --Output--

# Guess the number : 6
# lower than the given number


# Guess the number : 29
# higher than the given number


# Guess the number : 10
# You got the number