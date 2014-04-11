#!/usr/bin/env python3

import re

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
	i = input(

def endGame(state, score):
	print("supposed to end the jame... ^.^")

score = 0
state = readState()
print("Coin guessing game. All time high score: ", state[0], " correct by \"", state[1], "\".", sep="")
while flipCoin():
	score += 1
endGame(state, score)
