import random

user_score = 0
cpu_score = 0

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            cpu_score += 1
            print(str(cpu_score) + "-" + str(user_score))
        if computer == "scissor":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")
            user_score += 1
            print(str(cpu_score) + "-" + str(user_score))
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            cpu_score += 1
            print(str(cpu_score) + "-" + str(user_score))
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")
            user_score += 1
            print(str(cpu_score) + "-" + str(user_score))
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            cpu_score += 1
            print(str(cpu_score) + "-" + str(user_score))
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")
            user_score += 1
            print(str(cpu_score) + "-" + str(user_score))

    play_again = input("Wanna Play again?:").lower()
    if play_again != "yes":
        break
