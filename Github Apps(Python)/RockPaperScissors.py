import random
print("Winning rules of the game: \n" 
      +"Rock against Paper: Paper Wins!\n"
      +"Rock against Scissor: Rock Wins!\n"
      +"Paper against Scissor: Scissor Wins!\n")

while True:
    print("Enter your choice: \n"
          +"1. Rock\n"
          +"2. Paper\n"
          +"3. Scissor\n")
    
    choice = int(input("User turn: ")) 
    # takes input from user
    
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
    # looping until user enter invalid input 
    
    if  choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else: 
        choice_name = 'Scissor'
    # our user choice in an if else statement
    
    comp_choice = random.randint(1, 3)
    # the computers choice will be random
    
    while comp_choice == choice:
        comp_choice = random.randint(1 ,3)
    # we loop comp choice and equal it to choice 
    
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'
    # computers random choice in an if else statment
    
    print("Computer choice is: " + comp_choice_name) 
    print(choice_name + " vs " + comp_choice_name)  
    # these two prints show us our choice versus the computer
    
    if((choice == 1 and comp_choice == 2) or
       (choice == 2 and comp_choice == 1)):
            print("Paper wins => ", end = "") 
            result = "Paper"
    elif((choice == 1 and comp_choice == 3) or 
         (choice == 3 and comp_choice == 1)):
            print("Rock wins =>", end = "")
            result = "Rock"
    else:
        print("Scissor wins => ", end = "")
        result = "Scissor"
    # our winning conditions 
    
    if result == choice_name:
        print("\n------ USER WINS ------")
    else:
        print("\n------ COMP WINS ------")
    # our winning statement
        
    print("Do you want to play again? (Y/N)")
    ans = input()
    
    if ans == 'n' or ans == 'N':
        break
    # if the user does not want to play the end game message will play
    
    
print("\n Thank you for playing !")
    
        
    
        
        