#!/usr/bin/env python3

import re
from random import choice

def saveState(state):
	if state == []:
		return None
	f = open(".cointoss_save", "w")
	f.write(str(state[0]) + "\n" + state[1])
	f.truncate()
	f.close()

def readState():
	try:
		f = open(".cointoss_save", "r")
	except:
		return [0, "Nobody"]
	else:
		lines = f.readlines()
		f.close()
		return [int(lines[0]), lines[1]]

def flipCoin():
	i = input("Predict heads or tails: ")
	c = choice([True, False])

	if c:
		print("It is heads. ", end="")
	else:
		print("It is tails. ", end="")

	if (re.match(r"^[hH]", i) and c) or (re.match(r"^[tT]", i) and not c):
		return True
	else:
		return False

score = 0
state = readState()
print("Coin guessing game. All time high score: ", state[0], " correct by \"", state[1], "\".\n", sep="")
while flipCoin():
	score += 1
	print("Your score is: ", score, sep="")
print("Game over.\n")
name = input("What is your name: ")
if state[0] < score:
	state[0] = score
	state[1] = name
print("\nYour Score: ", score, "\tHigh Score: ", state[0])
saveState(state)
