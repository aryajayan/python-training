# Modify the Guessing Game to allow 3 tries for the user to guess the number right.

num=10
guessed=False

for i in range(3):
    guess_num=int(input("Guess the number : "))
    if guess_num>num:
        print("higher than the given number")
    elif guess_num<num:
        print("lower than the given number")
    else:
        guessed=True
        break

if guessed== True:
    print("Conngrats you got the number!")
else:
    print("Sorry better luck next time!")
    

# --Output--
# Guess the number : 6
# lower than the given number
# Guess the number : 4
# lower than the given number
# Guess the number : 7
# lower than the given number
# Soory better luck next time!

# Guess the number : 9
# lower than the given number
# Guess the number : 10
# Conngrats you got the number!