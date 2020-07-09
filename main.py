# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations
# to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import time


def verifyAnswer(choice1, choice2):
    if ((choice1.lower() == 'rock' and choice2.lower() == 'scissors')
        or (choice1.lower() == "scissors" and choice2.lower() == "paper")
            or (choice1.lower() == "paper" and choice2.lower() == "rock")):
        return 1

    else:
        return 0


def itsTie(choice1, choice2):
    if(choice1.lower() == choice2.lower()):
        return 1
    else:
        return 0


def endGame():
    playAgain = "y"
    playAgain = input("Do you wanna play again? (y/n): ")
    if (playAgain.lower() == "y"):
        return 1
    else:
        print("Shutting The Game Down...")
        time.sleep(2)
        exit()


def theWinnerIs(scorePlayer1, scorePlayer2, namePlayer1, namePlayer2):

    if scorePlayer1 > scorePlayer2:
        print("The winner is... " + namePlayer1)

    elif scorePlayer1 < scorePlayer2:
        print("The winner is... " + namePlayer2)

    else:
        print("There's no winner. It's a Tie")


def checkRounds(rounds):

    if (rounds == 0):
        print("The match is over")
        return 1
    else:
        return 0


def sumRounds(rounds):
    rounds = rounds - 1
    return rounds


def checkAll(rounds, scorePlayer1, scorePlayer2, namePlayer1, namePlayer2):

    if(checkRounds(rounds)):
        theWinnerIs(scorePlayer1, scorePlayer2,
                    namePlayer1, namePlayer2)
        if(endGame()):
            return 1

    else:
        return 0


def main():

    while True:

        namePlayer1 = input("Name Player1: ")
        namePlayer2 = input("Name Player2: ")
        print("\n")
        scorePlayer1 = 0
        scorePlayer2 = 0
        checkAnswer = 0

        rounds = int(input("Number of Rounds: "))
        print("\n")

        while rounds > 0:
            choicePlayer1 = input(
                "Player1, choose your element, Rock, Paper or Scissors: ")
            choicePlayer2 = input(
                "Player2, choose your element, Rock, Paper or Scissors: ")

            checkAnswer = itsTie(choicePlayer1, choicePlayer2)
            if(checkAnswer):
                print("You got a Tie\n")
                rounds = sumRounds(rounds)
                if(checkAll(rounds, scorePlayer1, scorePlayer2, namePlayer1, namePlayer2)):
                    break
                else:
                    continue

            checkAnswer = verifyAnswer(choicePlayer1, choicePlayer2)
            if (checkAnswer):
                scorePlayer1 = scorePlayer1 + 1
                print(namePlayer1 + " beat " + namePlayer2 + "\n")
                rounds = sumRounds(rounds)
                if(checkAll(rounds, scorePlayer1, scorePlayer2, namePlayer1, namePlayer2)):
                    break
                else:
                    continue

            checkAnswer = verifyAnswer(choicePlayer2, choicePlayer1)

            if (checkAnswer):
                scorePlayer2 = scorePlayer2 + 1
                print(namePlayer2 + " beat " + namePlayer1 + "\n")
                rounds = sumRounds(rounds)
                if(checkAll(rounds, scorePlayer1, scorePlayer2, namePlayer1, namePlayer2)):
                    break
                else:
                    continue


main()
