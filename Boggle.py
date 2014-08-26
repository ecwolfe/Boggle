#! /usr/bin/env python
# Ethan Wolfe

import sys
import random

usedDice = []

def beenUsed(count):
	for i in xrange(0,len(usedDice)):
		if (count == usedDice[i]):
			return True
	return False

def setupBoggle():

	board = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

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

		boggleBoard = [['' for y in xrange(4)] for x in xrange(4)]
	
		count = 0

		for l in xrange(0,4):
			for k in xrange(0,4):
				boggleBoard[l][k] = board[count]
				count += 1

	return boggleBoard

def getNeighbors(row, col):
	neigh = []
	for i in xrange(0,3):
		for j in xrange(0,3):
			newRow = (row - 1) + i
			newCol = (col - 1) + j
			if (newRow>0 and newRow<4 and newCol>0 and newCol<4):
				neigh.append([newRow,newCol])
	return neigh

def isWord(inWord):
	left = 0
	right = len(dictionary)

	while (left <= right):
		middle = (left + right)/2
		#print left
		#print right
		if( inWord > dictionary[middle] ):
			left = middle + 1
		elif( inWord < dictionary[middle] ):
			right = middle - 1
		else:
			return True

	return False

def wordSearch(x,y,testWord):
	if(len(testWord)>2):
		if(isWord(testWord)):
			if testWord not in solvedWords:
				solvedWords.append(testWord)
	if(len(testWord)>7):  # MAX_WORD_LENGTH
		return
	testWord += BoggleBoard[x][y]
	temp = BoggleBoard[x][y]
	BoggleBoard[x][y] = ''
	neighbors = getNeighbors(x,y)
	#print neighbors
	for p in xrange(0,len(neighbors)):
		a = neighbors[p][0]
		s = neighbors[p][1]
		if (len(BoggleBoard[a][s])>0):
			#print testWord
			wordSearch(a,s,testWord)
	BoggleBoard[x][y] = temp

def printBoard():
	for i in xrange(0,4):
		print '\n',
		for j in xrange(0,4):
			print BoggleBoard[i][j],
	print '\n',


dictionary = []
solvedWords = []

f = open ('sowpods.txt','r')

for line in f:
	dictionary.append(line.rstrip('\r\n'))

f.close()
 
BoggleBoard = setupBoggle()

#print BoggleBoard
#print dictionary

for l in xrange(0,4):
	for k in xrange(0,4):
		#print 'l = ' + str(l)
		#print 'k = ' + str(k)
		wordSearch(l,k,'')

#player's turn

printBoard()

print solvedWords





