import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number between 1 and " + str(x)  ))
        print(guess)
        if guess < random_number:
            print("sorry you too low")
        elif guess > random_number:
            print("sorry but you too high")

    print("Super you got it, the number was" + str(random_number))
        
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low , high)
        else:
            guess = low                       # could also be high b/c low high
        feedback = input("is " + str(guess)+"too high (H), too low (L), correct (c)?? " ).lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("Gongrats you got it, the number was" + str(guess) + ".")         



computer_guess(1000)




