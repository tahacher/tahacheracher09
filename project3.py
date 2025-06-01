import random 

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    answer = input("Type rock/paper/scissors or Q to quit: ").lower()

    if answer == "q":
        print("Goodbye!")
        break

    if answer not in options:
        print("Invalid choice, please try again.")
        continue

    computer_pick = random.choice(options)  # Computer selects a random choice
    print(f"Computer picked {computer_pick}.")

    # Determine the winner
    if (answer == "rock" and computer_pick == "scissors") or \
       (answer == "paper" and computer_pick == "rock") or \
       (answer == "scissors" and computer_pick == "paper"):
        print("You win!")
        user_wins += 1
    elif answer == computer_pick:
        print("It's a tie!")
    else:
        print("You lose!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print("Goodbye!")
