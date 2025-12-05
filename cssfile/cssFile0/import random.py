import random

random_to_guess = random.randint(1,100)

while True:
      try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < random_to_guess:
           print("Too low!")
        elif guess > random_to_guess:   
             print("Too High!")
        else:
            print("congratulation! you have guessed the number")
            break
      except ValueError:
          print("You Entered invalid input")
