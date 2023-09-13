#program for rock-paper-scissors game
import random
user_score = 0
computer_score = 0

def play_game():
    global user_score
    global computer_score
    choices=["rock","paper", "scissors:"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    print("You chose:" ,user_choice)
    print("Computer chose:",computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
        ):
        print(" Congratulations!!! You win!")
        user_score += 1
    else:
        print("Sorry!!! you lost!")
        computer_score += 1
    print("Your score:",user_score)
    print(" Computer score:",computer_score)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again== "yes":
        play_game()
    else:
        print("Thankyou for playing!")
play_game()

