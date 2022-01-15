import random 

name = input("What is your name? ") 
# we ask the users name

print("Good Luck! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words) 
# uses the list of words above and picks one for the user to guess

print ("Guess the characters")

guesses = ''

turns = 10

while turns > 0:
    
    failed = 0
    # this is a counter to show how many times the user has failed so far
    
    for char in word:
        if char in guesses:
            print(char)
            
        else:
                print("_")
                failed += 1
                # everytime the user fails, the fail counter goes up by one
                
    if failed == 0:
        print("You Win!")
        
        print("The word is: ", word)
        break
    
    guess = input("guess a character: ")
    guesses += guess 
    # this is where our guesses are being stored 
    
    if guess not in word:
        turns -= 1
        # everytime a user inputs the wrong guess, a turn is taken away
        
        print("Wrong")
        
        print("You have", + turns, 'more guesses')
        # shows the user how many turns they have left 
        
        if turns == 0:
            print("You Lose!")
            # if no turns left you lose