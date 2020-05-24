import time
import random

print("Welcome players to the first Rock Paper Scissors World Cup! I am your host,\n Professor Python McDerpface!\n in the ...")
time.sleep(3)

print("ROCK....")
time.sleep(1)
print("PAPER....")
time.sleep(1)
print("SCISSORS....")
time.sleep(1)
print("SHOW!!!!!!")
time.sleep(1)
print("Ready Player 1!")
time.sleep(2)
while True:
	player1 = input("Please enter your choice: rock, paper or scissors? (or quit with \"q\") ").lower()
	if player1 == 'q':
		break
	computer = random.choice(["rock","paper","scissors"])
	time.sleep(1)
	print(f"Player picks {player1}!")
	print("Computer picks " + computer + "!")
	if player1:
		if player1 == computer:
			print("It's a Draw!")
		elif player1 == "rock":
			if computer == "paper":
				print("Computer wins! Paper wraps rock!")
			else:
				print("Player 1 wins! Rock smashes scissors!")
		elif player1 == "paper":
			if computer == "rock":
				print("Player 1 wins! Paper wraps rock!")
			else:
				print("Computer wins! Scissors cut paper!")
		elif player1 == "scissors":
			if computer == "rock":
				print("Computer wins! Rock smashes scissors!")
			else:
				print("Player 1 wins! Scissors cut paper!")
		else:
			print(f"Nice try, but {player1} is not a valid pick! Pick rock, paper or scissors!")
	else:
		print("You can't play with an empty hand, Player1! Pick rock, paper or scissors!")
time.sleep(1)
print("Thanks for playing! Bye!")

