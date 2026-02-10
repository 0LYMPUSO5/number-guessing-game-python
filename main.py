import random as ran

guessed_number = ran.randint(1, 100)
NumberOfDraw = 0
Number = -1
while Number != guessed_number:
    
    Number = int(input("Guess the number: "))
    if Number > guessed_number:
        print("Enter Lower number")
    elif Number < guessed_number:
        print("Enter Higher number")

    NumberOfDraw += 1

print(f"You have guessed the right number, number is {guessed_number} and number of drawn is {NumberOfDraw}")

