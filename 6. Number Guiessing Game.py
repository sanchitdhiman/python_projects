def guessed(num, count):
    print(f"Congratulations! You guessed the number. The number was {num}. You guessed it in {count} tries.")

    re = input("\nDo you want to play again? (y/n): ")
    if re.lower() == 'y':
        game()
    else:
        print("\nThank you for playing!")

def guessing(num, guess, count):
    if guess == num:
        guessed(num, count)
        return
    
    if guess < num:
        print("\nLOW.")
    else:
        print("\nHIGH")

    guess = int(input("Enter you next guess: "))
    guessing(num, guess, count + 1)
    

def game():
    start = int(input("\nEnter the starting number of the range: "))
    end = int(input("Enter the ending number of the range: "))

    import random
    random_number = random.randint(start, end)

    print("\nAlright! Let's start the game!\n")

    guess = int(input("Enter your guess: "))
    guessing(random_number, guess, 0)

print("Welcome to the Number Guessing Game!")

print("\nRules:\n1. You have to tell the range in which you'll be guessing.\n2. The computer will generate a random number in that range.\n3. You have to guess the number.\n4. You'll be given hints if your guess is high or low.\n5. You have to guess the number in minimum number of tries.")

game()