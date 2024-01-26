import random 
import time
import os

while True:
    os.system('cls')
    time.sleep(1)
    print("\n\n ******* WELCOME TO ROCK PAPER SCISSOR GAME *******\n\n")
    print("Winning Rules of the Rock paper scissor game as follows: \n"+"Rock vs Paper->Paper wins \n"+ "Rock vs Scissor->Rock wins \n"+"Paper vs Scissor->Scissor wins \n") 
    print("Enter choice \n 1. Rock \n 2. Paper \n 3. Scissor \n")
    
    # acceptables=[1,2,3]
    # take the input from user
    while True :
        i = input(" User turn: ")
        try:
            if i == "":
                print(" No Data found")
            else :
                choice = int(i)
                break
        except ValueError:
            print(" Enter valid input") 
    # OR is the short-circuit operator 
    # if any one of the condition is true 
    # then it return True value 
    # looping until user enter invalid input 
    while choice > 3 or choice < 1: 
        choice = int(input(" Enter valid input: ")) 
    # initialize value of choice_name variable 
    # corresponding to the choice value 

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2: 
        choice_name = 'Paper'
    else: 
        choice_name = 'Scissor'
          
    # print user choice  
    print("\n User choice is : " + choice_name) 
    print("\n Now its Computer turn...") 
    time.sleep(2)
    # Computer chooses randomly any number  
    # among 1 , 2 and 3. Using randint method 
    # of random module 
    comp_choice = random.randint(1,3) 
      
    # looping until comp_choice value  
    # is equal to the choice value 
    #while comp_choice == choice: 
    #    comp_choice = random.randint(1,3) 
  
    # initialize value of comp_choice_name  
    # variable corresponding to the choice value 
    time.sleep(2)
    if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'Paper'
    elif comp_choice == 3:
        comp_choice_name = 'Scissor'
    print("\n Computer choice is: " + comp_choice_name) 
  
    print(" "+ choice_name + " V/s " + comp_choice_name) 
    
    # condition for winning 
    time.sleep(2)
    if choice == comp_choice:
        print("Tie")
        result = "Tie"
    elif((choice == 1 and comp_choice == 2) or
          (choice == 2 and comp_choice ==1 )): 
        print("\n <=== Paper wins ===> ", end = "") 
        result = "Paper"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        print("\n <=== Rock wins ===> ", end = "") 
        result = "Rock"
    elif((choice == 2 and comp_choice == 3) or
        (choice == 3 and comp_choice == 2)):
        print("\n <=== Scissor wins ===> ", end = "") 
        result = "Scissor"
        
    # Printing either user or computer wins 
    if result == choice_name: 
        print("\n <**** User wins ****>") 
    elif result == comp_choice_name:    
        print("\n <**** Computer wins ****>")
    elif result == "Tie":
        print("\n TIE ")
        
    time.sleep(2)     
    print("Do you want to play again? (Y/N)") 
    ans = input() 
    # if user input n or N then condition is True 
    if ans == 'n' or ans == 'N':
        print("\n Thanks for playing")    
        
# after coming out of the while loop 
# we print thanks for playing 
