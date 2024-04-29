import random
user_action = input("Enter an action (rock,paper,scissor):")
possibilities = ["rock","paper","scissor"]
computer_action = random.choice(possibilities)
if user_action == computer_action:
    print("Tie")
elif user_action == "rock":
    if computer_action == "scissor":
        print("Rock hits the Scissor and You win!")
    else:
        print("Paper covers the Rock and Computer wins!")
elif user_action == "paper":
    if computer_action == "scissor":
        print("Scissor cuts the Paper and Computer wins!")    
    else:
        print("Paper covers the Rock and You win!")
elif user_action == "scissor":  
    if computer_action == "paper":
        print("Scissor cuts the Paper and You win!")  
    else:
        print("Rock hits the Scissor and Computer wins!")