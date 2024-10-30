guessNumber = 12
timesPlay = 0

try:
    inputNumber = int(input("Guess the number: "))
    if(inputNumber < 50 and inputNumber > 10):
        while(inputNumber != guessNumber):
            timesPlay += 1
            if(timesPlay == 3):
                print("############################################")
                print("###Sorry! You have exhausted your trials.###")
                print("############################################")
                confirm = input("Do you want to Play Again? (yes/no): ")
                if(confirm == 'yes'):
                    timesPlay = 0
                    inputNumber = int(input("Guess the number: "))
                else:
                    break
            else:
                if(inputNumber < guessNumber):
                    print("Try a higher number.")
                    inputNumber = int(input("Guess the number: "))
                else:
                    print("Try a lower number.")
                    inputNumber = int(input("Guess the number: "))

        print("############################################")
        print("###Congratulations! You guessed it right.###")
        print("############################################")  
    else:
        print("Please enter a number between 10 and 50.")                
  
except ValueError:
    print("Please enter a valid number.")

