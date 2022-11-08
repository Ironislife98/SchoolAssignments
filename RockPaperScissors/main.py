import random

print("Rock-Paper-Scissors is a game played between two individuals. The rules of the game are:\n")
print("Rock breaks Scissors,\nScissors cut Paper, and \nPaper covers Rock.")


w, l, t = 0, 0, 0

def determine_outcome(user, comp):
  pass


def RockPaperScissors(n=0):
  options = ["rock","paper", "scissors"]
  if n == 0:
    playerChoice = input("Enter choice: ")
    compChoice = options[random.randint(0, 2)]
    determine_outcome(playerChoice, compChoice)
  else: