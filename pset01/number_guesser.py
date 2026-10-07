import random 

print("Welcome toooooo... *drum roll* El's NUMBER GUESSER!!!")
print("A random number from 1 to 1000 has been generated.")

random_number = random.randint(1, 1000)
incorrect_guesses = 0

while True:
    print("")
    print("If you wish to leave, type \'bye\' or \'exit\'.")
    guess = input("Type your number guess: ").strip().lower()

    if guess == "bye" or guess == "exit":
        print("Aww... Goodbye then :(")
        break
    else: 
        try:
            guess_number = int(guess)
            if guess_number == random_number:
                print(f"YOU DID IT!!! CONGRATS!! YOU GUESSED THE NUMBER!!! Your number of tries was {incorrect_guesses}.")
                print("Now do it again! A new number has been generated :)")
                random_number = random.randint(1, 1000)
                incorrect_guesses = 0
            elif guess_number < random_number:
                print("Oohhh... Too low! Try again!")
                incorrect_guesses += 1
            else:
                print("Yikes... Too high! Try again!")
                incorrect_guesses += 1
        except ValueError:
            print("That is NOT a valid number. Please keep your input digits ONLY!!")

  