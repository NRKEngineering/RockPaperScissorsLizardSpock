#! /usr/bin/python
import random
import getpass
import curses

# Setup Params
mainBorder = 0
strList = ["rock", "Rock", "paper", "Paper", "scissors", "Scissors", "lizard", "Lizard", "spock", "Spock"]
pythonType = "Python 2"
#pythonType = "Python 3"

#******** Decision functions ******************************************************************************************
# Scissors
def ScissorsCutsspaper(winner, loser):
	return ("Scissors cuts paper")

def ScissorsDecapitateslizard(winner, loser):
	return ("Scissors decapitates lizard")
	
def ScissorsDraw():
	return ("Its a draw. Looks like you are not ... cut out ... to play this game")
	
# Paper
def PaperCoversRock(winner, loser):
	return ("Paper covers rock")
	
def PaperDisprovesSpock(winner, loser):
	return ("Paper disproves Spock")
	
def PaperDraw():
	return ("Its a draw. Both of you seems to be reading from the same page.")
	
# Rock
def RockCrushesLizard(winner, loser):
	return ("Rock crushes lizard")
	
def RockCrushesScissors(winner, loser):
	return ("Rock crushes scissors")
	
def RockDraw():
	return ("Its a draw. Don't worry, you can just tell everyone you're both winners")

# Lizard
def LizardPoisonsSpock(winner, loser):
	return ("Lizard posions Spock")
	
def LizardEatsPaper(winner, loser):
	return ("Lizard eats paper")
	
def LizardDarw():
	return ("And the winner is.... oh, its a draw. How disappointing")
	
# Spock
def SpockVaporisesRock(winner, loser):
	return ("Spock vaporises rock")
	
def SpockSmashesScissors(winner, loser):
	return ("Spock smashes scissors")
	
def SpockDraw():
	return ("Its a draw. Guys please, we can't all be Spock")
	

#******** Compare answers function ************************************************************************************
def compare(player1, player2):
	
	if ("cissors" in player1):
		if ("cissors" in player2):
			endMsg = ScissorsDraw()
		if ("aper" in player2):
			endMsg = ScissorsCutsspaper(player1, player2)
		if ("rock" in player2) or ("Rock" in player2):
			endMsg = RockCrushesScissors(player2, player1)
		if ("izard" in player2):
			endMsg = ScissorsDecapitateslizard(player1, player2)
		if ("pock" in player2):
			endMsg = SpockSmashesScissors(player2, player1)
	elif ("aper" in player1):
		if ("cissors" in player2):
			endMsg = ScissorsCutsspaper(player2, player1)
		if ("aper" in player2):
			endMsg = PaperDraw()
		if ("rock" in player2) or ("Rock" in player2):
			endMsg = PaperCoversRock(player1, player2)
		if ("izard" in player2):
			endMsg = LizardEatsPaper(player1, player2)
		if ("pock" in player2):
			endMsg = SpockSmashesScissors(player2, player1)
	elif ("rock" in player1) or ("Rock" in player1):
		if ("cissors" in player2):
			endMsg = RockCrushesScissors(player1, player2)
		if ("aper" in player2):
			endMsg = PaperCoversRock(player2, player1)
		if ("rock" in player2) or ("Rock" in player2):
			endMsg = RockDraw()
		if ("izard" in player2):
			endMsg = RockCrushesLizard(player1, player2)
		if ("pock" in player2):
			endMsg = SpockVaporisesRock(player2, player1)
	elif ("izard" in player1):
		if ("cissors" in player2):
			endMsg = ScissorsDecapitateslizard(player2, player1)
		if ("aper" in player2):
			endMsg = LizardEatsPaper(player1, player2)
		if ("rock" in player2) or ("Rock" in player2):
			endMsg = RockCrushesLizard(player2, player1)
		if ("izard" in player2):
			endMsg = LizardDarw()
		if ("pock" in player2):
			endMsg = LizardPoisonsSpock(player1, player2)
	elif ("pock" in player1):
		if ("cissors" in player2):
			endMsg = SpockSmashesScissors(player1, player2)
		if ("aper" in player2):
			endMsg = PaperDisprovesSpock(player2, player1)
		if ("rock" in player2) or ("Rock" in player2):
			endMsg = SpockVaporisesRock(player1, player2)
		if ("izard" in player2):
			endMsg = LizardPoisonsSpock(player2, player1)
		if ("pock" in player2):
			endMsg = SpockDraw()
	
	finalString = "Player one chose " + str(player1) + " Player two chose "  + str(player2)
	screen.clear()
	screen.border(mainBorder)
	screen.addstr(2, 2, finalString)
	screen.addstr(4, 2, endMsg)
	screen.refresh()

#******** Get User Input **********************************************************************************************
def Get_User_Input():
	userInput = screen.getstr(10, 10, 60)
	if any([s in userInput for s in strList]):
		return userInput
	else:
		Get_User_Input()
	
#******** Main Menu ***************************************************************************************************
def menu():
	menuChoice = 0	
	
	# Draw the main menu
	screen.clear()
	screen.border(mainBorder)
	screen.addstr(2, 20, "ROCK PAPER SCISSOR LIZARD SPOCK", curses.A_UNDERLINE)
	screen.addstr(3, 2, "Please enter a number...")
	screen.addstr(5, 4, "1 - Start Game")
	screen.addstr(6, 4, "2 - Rules")
	screen.addstr(7, 4, "3 - Credits")
	screen.addstr(8, 4, "4 - Exit")
	screen.refresh()

	menuChoice = screen.getch()	# User menu selection

	if menuChoice == ord('1'):	# Starts game
		gameLoop()
	if menuChoice == ord('2'):	# Goes to "Rules" page
		rules()
	if menuChoice == ord('3'):	# Goes to "Credits" page
		credits()      
	if menuChoice == ord('4'):	# Quits out of program ( immeadiatly at the moment, will put a y/n in at some point)
		quitOut()
		return		# Exits to end of program
		
#******** Main Game loop **********************************************************************************************
def gameLoop():
	playAgain = "yes"
	while playAgain == "yes":

	# PLayer1's turn
		screen.clear()
		screen.border(mainBorder)
		screen.addstr(2, 2, "Player 1, you go first.")
		screen.addstr(3, 2, "What will it be? rock, paper, sicssors, lizard or spock?")
		screen.refresh()
		player1 = str(Get_User_Input())

	# Player2's turn
		screen.clear()
		screen.border(mainBorder)
		screen.addstr(2, 2, "Thankyou player1, nows its player2's turn")
		screen.addstr(3, 2, "What will it be? rock, paper, sicssors, lizard or spock?")
		screen.refresh()
		player2 = str(Get_User_Input())
		
	# Compare Result
		screen.clear()
		screen.border(mainBorder)
		screen.addstr(2, 2, "Thankyou player2, now lets see who is the winner. Press enter to find out")
		screen.refresh()
		screen.getstr(10, 10, 60)
		
		compare(player1, player2)

		# Give user choice to play again
		screen.addstr(10, 2, "Would you like to play again?")
		playAgain = screen.getstr(11, 10, 60)

		if ('Y' in str(playAgain)) or ('y' in str(playAgain)):
			gameLoop()
		else:
			quitOut()

#******** Rules Function **********************************************************************************************
def rules():
	
	screen.clear()
	screen.border(mainBorder)
	screen.addstr(2, 5, "*************   The Rules   *************")
	screen.addstr(3, 2, "	- Scissors cuts Paper,")
	screen.addstr(4, 2, "	- Paper covers rock,")
	screen.addstr(5, 2, "	- Rock crushes lizard,")
	screen.addstr(6, 2, "	- Lizard posions spock,")
	screen.addstr(7, 2, "	- Spock smashes scissors,")
	screen.addstr(8, 2, "	- Scissors decapitates lizard,")
	screen.addstr(9, 2, "	- Lizard eats paper,")
	screen.addstr(10, 2, "	- Paper disproves spock,")
	screen.addstr(11, 2, "	- Spock vaporises rock,")
	screen.addstr(12, 2, "	- (and as it always has) Rock crushes scissors.")
	screen.getstr(14, 10, 60)
	menu()

#******** Credits function ********************************************************************************************
def credits():
	screen.clear()
	screen.border(mainBorder)
	screen.addstr(2, 5, "*************   Credits   *************")
	screen.getstr(14, 10, 60)
	menu()

#******** Quit function ***********************************************************************************************
def quitOut():
	curses.endwin()
	quit()	

# Program starts here
screen = curses.initscr()	# Initiate curses window
curses.curs_set(0)		# Turn curser to invisible
menu()

curses.endwin() # Make sure window is ended so you can continue to use the terminal

