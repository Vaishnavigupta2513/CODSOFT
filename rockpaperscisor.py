import random
options = ["Rock","Paper","Scissors"]
while True:
    player_choice = input("Chosse Rock,Paper or Scissors:")
    computer_choice = random.choice(options)
    print("Your Choice",player_choice)
    print("Computer Choice",computer_choice)
    if player_choice == computer_choice:
        print("It's Tie")
    elif player_choice == "Rock" and computer_choice == "Scissors":
        print("You Win!!")
    elif player_choice == "Paper" and computer_choice == "Rock":
        print("You Win!!")
    elif player_choice == "Scissor" and computer_choice == "Paper":
        print("You Win!!")
    else:
        print("Computer Wins!!")
    repeat = input("Do you want to play again?(yes/no):")
    if repeat == "yes":
        print("Thank You For Playing")
        break
    