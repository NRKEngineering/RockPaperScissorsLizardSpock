#! /usr/bin/python
import random
import getpass

#pythonType = "Python 2"
pythonType = "Python 3"

#print(chr(27) + "[2J")
print ("\n\n\nWelcome to Rock, Paper, Scissors, Lizard, Spock\n\n")

# Decision function
# Scissors
def ScissorsCutsspaper(winner, loser):
	print ("\nScissors cuts paper")
	return
def ScissorsDecapitateslizard(winner, loser):
	print ("\nScissors decapitates lizard")
	return
def ScissorsDraw():
	print ("\nIts a draw. Looks like you are not ... cut out ... to play this game")
	return

# Paper
def PaperCoversRock(winner, loser):
	print ("\nPaper covers rock")
	return
def PaperDisprovesSpock(winner, loser):
	print ("\nPaper disproves Spock")
	return
def PaperDraw():
	print ("\nIts a draw. Both of you seems to be reading from the same page.")
	return

# Rock
def RockCrushesLizard(winner, loser):
	print ("\nRock crushes lizard")
	return
def RockCrushesScissors(winner, loser):
	print ("\nRock crushes scissors")
	return
def RockDraw():
	print ("\nIts a draw. Don't worry, you can just tell everyone you're both winners")
	return

# Lizard
def LizardPoisonsSpock(winner, loser):
	print ("\nLizard posions Spock")
	return
def LizardEatsPaper(winner, loser):
	print ("\nLizard eats paper")
	return
def LizardDarw():
	print ("\nAnd the winner is.... oh, its a draw. How disappointing")
	return

# Spock
def SpockVaporisesRock(winner, loser):
	print ("\nSpock vaporises rock")
	return
def SpockSmashesScissors(winner, loser):
	print ("\nSpock smashes scissors")
	return
def SpockDraw():
	print ("\nIts a draw. Guys please, we can't all be Spock")
	return

#******** Compare answers function ************************************************************************************
def compare(player1, player2):
	print ("Player one chose " + player1 + "\n" + "Player two chose "  + player2)
	
	if player1 == "scissors":
		if player2 == "scissors":
			ScissorsDraw()
		if player2 == "paper":
			ScissorsCutsspaper(player1, player2)
		if player2 == "rock":
			RockCrushesScissors(player2, player1)
		if player2 == "lizard":
			ScissorsDecapitateslizard(player1, player2)
		if player2 == "spock":
			SpockSmashesScissors(player2, player1)
	elif player1 == "paper":
		if player2 == "scissors":
			ScissorsCutsspaper(player2, player1)
		if player2 == "paper":
			PaperDraw()
		if player2 == "rock":
			PaperCoversRock(player1, player2)
		if player2 == "lizard":
			LizardEatsPaper(player1, player2)
		if player2 == "spock":
			SpockSmashesScissors(player2, player1)
	elif player1 == "rock":
		if player2 == "scissors":
			RockCrushesScissors(player1, player2)
		if player2 == "paper":
			PaperCoversRock(player2, player1)
		if player2 == "rock":
			RockDraw()
		if player2 == "lizard":
			RockCrushesLizard(player1, player2)
		if player2 == "spock":
			SpockVaporisesRock(player2, player1)
	elif player1 == "lizard":
		if player2 == "scissors":
			ScissorsDecapitateslizard(player2, player1)
		if player2 == "paper":
			LizardEatsPaper(player1, player2)
		if player2 == "rock":
			RockCrushesLizard(player2, player1)
		if player2 == "lizard":
			LizardDarw()
		if player2 == "spock":
			LizardPoisonsSpock(player1, player2)
	elif player1 == "spock":
		if player2 == "scissors":
			SpockSmashesScissors(player1, player2)
		if player2 == "paper":
			PaperDisprovesSpock(player2, player1)
		if player2 == "rock":
			SpockVaporisesRock(player1, player2)
		if player2 == "lizard":
			LizardPoisonsSpock(player2, player1)
		if player2 == "spock":
			SpockDraw()
			
#******** Main Menu ***************************************************************************************************
def menu():
	print ("\n                 *************   Main Menu   *************")
	print ("\n" * 5)
	print ("1) Start Game\n")
	print ("2) Rules\n")
	print ("3) Credits\n")
	print ("\n" * 9)
	# Menu user choice
	if(pythonType == "Python 2"):	# Python 2
			menuInput = raw_input ("Please make a selection: ")
	elif(pythonType == "Python 3"):	# Python 3
			menuInput = input("Please make a selection: ")
			
	if(menuInput == "1"):		# Play game
		gameLoop()
	elif(menuInput == "2"):	# Rules
		rules()
	elif(menuInput == "3"):	# Credits
		credits()
		
#******** Main Game loop **********************************************************************************************
def gameLoop():
	playAgain = "yes"
	while playAgain == "yes":

	# PLayer1's turn
		print ("Player 1, you go first.")
		print ("\n" * 15)
		player1 = input ("What will it be? rock, paper, sicssors, lizard, spock?" + "\n"* 23 + ": ")
		#player1 = getpass.getpass("What will it be? rock, paper, scissors, lizard, spock? \n\n")
		
		#while (player1 == "rock" and player1 == "paper" and player1 == "scissors" and player1 == "lizard" and player1 == "spock")
		
		#print(chr(27) + "[2J")	# Clear the screen
	
		print ("\n\nThankyou player1, nows its player2's turn\n")
		
		player2 = input ("What will it be? rock, paper, sicssors, lizard, spock? \n\n" + "\n" * 19 + ": ")
		#player2 = getpass.getpass("What will it be? rock, paper, scissors, lizard, spock?\n\n")

		#print(chr(27) + "[2J")	# Clear the screen
		print ("\n" * 15)
		#raw_input("Thankyou player2, now lets see who is the winner. Press enter to find out")
		input("Thankyou player2, now lets see who is the winner. \n\nPress enter to find out" + "\n" * 21 + " ")
		
		#print(chr(27) + "[2J")	# Clear the screen
		print ("\n\n\n")
		compare(player1, player2)
		print ("\n" * 15)
		
		# Give user choice to play again
		if(pythonType == "Python 2"):	# Python 2
			playAgain = raw_input ("\n\n\nWould you like to play again? ")
		elif(pythonType == "Python 3"):	# Python 3
			playAgain = input("\n\n\nWould you like to play again?")

#******** Rules Function **********************************************************************************************
def rules():
	print("\n                 *************   The Rules   *************")
	print("""\n\n	- Scissors cuts Paper,
	- Paper covers rock,
	- Rock crushes lizard,
	- Lizard posions spock
	- Spock smashes scissors,
	- Scissors decapitates lizard,
	- Lizard eats paper,
	- Paper disproves spock,
	- Spock vaporises rock,
	- (and as it always has) Rock crushes scissors.\n""")
	print("\n"*8)
	
	if(pythonType == "Python 2"):	# Python 2
			rulesInput = raw_input ("Return to main menu (y/n): ")
	elif(pythonType == "Python 3"):	# Python 3
			rulesInput = input("Return to main menu (y/n): ")
	if(rulesInput == "y"):
		menu()
#******** Credits function ********************************************************************************************
def credits():
	print("\n                 *************   Credits   *************")
	print ("\n" * 21)
	if(pythonType == "Python 2"):	# Python 2
			creditsInput = raw_input ("Return to main menu (y/n): ")
	elif(pythonType == "Python 3"):	# Python 3
			creditsInput = input("Return to main menu (y/n): ")
	if(creditsInput == "y"):
		menu()


# Program starts here

menu()

