import random

print("1: Rock | 2: Paper | 3: Scissors")

while True:
    ci = random.randint(1, 3)  # Computer's choice
    try:
        piN = int(input("Enter your choice (1/2/3): "))  # Player's choice
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        continue

    print(f"Computer chose: {ci}")

    if piN == 1 and ci == 2:  
        print("You chose Rock and Computer chose Paper.")
        print("You got covered by paper.\nYou lost!")
    
    elif piN == 2 and ci == 1:
        print("You chose Paper and Computer chose Rock.")
        print("You covered the rock.\nYou won!")

    elif piN == 2 and ci == 3:
        print("You chose Paper and Computer chose Scissors.")
        print("Computer cut you down.\nYou lost!")

    elif piN == 3 and ci == 2:
        print("You chose Scissors and Computer chose Paper.")
        print("You tore down the computer.\nYou won!")

    elif piN == 3 and ci == 1:
        print("You chose Scissors and Computer chose Rock.")
        print("You got crushed by rock.\nYou lost!")

    elif piN == 1 and ci == 3:
        print("You chose Rock and Computer chose Scissors.")
        print("You smashed the scissors.\nYou won!")

    else:
        print("Invalid choice, please enter 1, 2, or 3.")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
