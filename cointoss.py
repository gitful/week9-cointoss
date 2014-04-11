#!/usr/bin/env python3

import re
from random import choice

def saveState(state):
	if state == []:
		print("You didn't even play. Sucker.")

def readState():
	f = open(".cointoss_save", "r")
	lines = f.readlines()
	f.close()
	if lines == []:
		return []
	return [lines[0], lines[1]]

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

def endGame(state, score):
	print("supposed to end the jame... ^.^")

score = 0
state = readState()
print("Coin guessing game. All time high score: ", state[0], " correct by \"", state[1], "\".", sep="", end="\n\n")
while flipCoin():
	score += 1
endGame(state, score)
