#! /usr/bin/env python
# Ethan Wolfe

import sys
import random

def beenUsed(count):
	for i in xrange(0,len(usedDice)):
		if (count == usedDice[i]):
			return True
	return False


board = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

usedDice = []

dice =  ['FORIXB', 'MOQABJ', 'GURILW', 'SETUPL', 'CMPDAE', 'ACITAO', 'SLCRAE', 'ROMASH', 'NODESW', 'HEFIYE', 'ONUDTK', 'TEVIGN', 'ANEDVZ', 'PINESH', 'ABILYT', 'GKYLEU']

for i in xrange(0,16):
	rDie = random.randrange(0,16)
        rPos = random.randrange(0,16)

	if i > 0:
		while ((board[rPos] != '') | beenUsed(rDie)):
			rDie = random.randrange(0,16)
			rPos = random.randrange(0,16)

	usedDice.append(rDie)

	rFace = random.randrange(0,6)
	board[rPos] = dice[rDie][rFace]

# Print board

for i in xrange(1,17):
	print board[i-1],
	if (i % 4 == 0):
		print '\n'




