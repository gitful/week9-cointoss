#!/usr/bin/env python3

import re

def saveState(state):
	print("supposed to save state")

def readState():
	print("supposed to read state")

def flipCoin(state):
	print("flipping the coin, matey")

def endGame(state):
	print("supposed to end the jame... ^.^")

state = readState()
while True:
	if not flipCoin(state):
		endGame(state)
