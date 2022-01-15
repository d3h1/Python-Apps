import random
import math 

lower = int(input("Enter Lower Bounds:- "))

upper = int(input("Enter Upper Bounds:- "))


x = random.randint(lower, upper)
print("\n\tYou only have ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")

count = 0



while count < math.log(upper - lower + 1, 2):
    count += 1
    
    
    guess = int(input("Guess a number:- "))
    
    
    if x == guess:
        print("Congratulations you did it in ",
            count, " try's")
        
        break
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print("You guess too high")
        
        
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")
