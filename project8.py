import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def check_guess(guess, target):
    #Compare guess to the target number.
    if guess > target:
        print("Too high!!")
        return False
    elif guess < target:
        print("Too low!!")
        return False
    else:
        print("You got it. the number was {target}")
        return True
    

    
def choose_difficulty():
    #Ask the user to choose the difficulty and return  attempt allowed
    while True:
        level = input("choose your difficulty. Type 'hard'or'easy'").lower()
        if level == "easy":
            return EASY_ATTEMPTS
        elif level == "hard":
            return HARD_ATTEMPTS
        else:
            print("Invalid choice.Please type 'easy'or'hard'")


def game():
    print("Hello Im TAHA ,welcom to your game")
    print("Im thinking a number between 1 and 100")
    target = random.randint(1,100)
    attempt = choose_difficulty()
    guessed_correctly = False


    while attempt > 0 and not guessed_correctly:
      print("\nYou have " + str(attempt) + " attempts remaining.")
      try:
       guess = int(input("Make a guess: "))
      except ValueError as e:
          print("please enter a valid number:", e)
          continue
      
      guessed = check_guess(guess, target)
      if not guessed:
          attempt - 1


    if not guessed:
        print("\nOut of attempts!! the number was "+str(target))

          
          


