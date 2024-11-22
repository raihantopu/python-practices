import random

def main():
    print("Welcome to number guessing game........")
    playAgain = "y"
    while playAgain == "y" or playAgain == "Y":
        startGame()
        playAgain = input("Do you want to play again? 'y for yes' other key for no: ")

def startGame():
    #taking value from the user for the random function range start, end. From which a random number will be generated
    start = takeInputFromUser("Enter the start range of the random num: ")
    end = takeInputFromUser("Enter the end range of the random num: ")
    #generating random number from the user inputs
    rndNumber = random.randrange(start, end)
   
    numOfAttemptTaken = matchTheNumber(rndNumber, start, end)
    print(f"You have guessed the right number, your total attempt is: {numOfAttemptTaken}")

def matchTheNumber(rndNumber, start, end):
    #taking the first guess from the user
    inputValue = takeInputFromUser(f"Guess the number between {start}, {end} : ")
    attemptCount = 1
    while rndNumber != inputValue:
        if rndNumber > inputValue:
            attemptCount += 1
            inputValue = takeInputFromUser("Nubmer is not correct, Guess a higher number: ")
        else:
            attemptCount += 1
            inputValue = takeInputFromUser("Number is not correct, Guess a lower number: ")
    
    return attemptCount

#input function which will catch error while input other than number
def takeInputFromUser(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please input an integer number!!!!")

#calling the main function
main()