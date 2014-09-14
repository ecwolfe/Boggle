#! /usr/bin/env python
# Ethan Wolfe

import sys
import random

class Boggle:
	dictionary = []									# Legal words to use
	solvedWords = []								# legal words with this board
	boggleBoard = []								# The 2-D storage of the board

	def __init__(self):								# Starts each game by making a board

		# The second dice has Q instead of Qu
		dice =  ['FORIXB', 'MOQABJ', 'GURILW', 'SETUPL', 'CMPDAE', 'ACITAO', 'SLCRAE', 'ROMASH', 'NODESW', 'HEFIYE', 'ONUDTK', 'TEVIGN', 'ANEDVZ', 'PINESH', 'ABILYT', 'GKYLEU']
		
		results = [d[random.randrange(0,6)] for d in dice]  			# Creates a List of 16 letters from a random char in each dice  
		random.shuffle(results)							# The randomly shuffles order of the dice

		self.boggleBoard = [['' for y in xrange(4)] for x in xrange(4)]		# Makes a 2-D board

		count = 0

		for l in xrange(0,4):
			for k in xrange(0,4):
				self.boggleBoard[l][k] = results[count]			# Loads randomized letters from each dice into 2-D board
				count += 1
		
		
	def getBoard(self):
		return self.boggleBoard

	def printBoard(self):
		for l in xrange(0,4):
			for k in xrange(0,4):
				print self.boggleBoard[l][k],
			print '\n'
		print '\n'
		

	def clearWordList(self):
		self.solvedWords = []
		words = []

	def getNeighbors(self,row, col):							# Gets list of neighbors + self from a 2-D grid.
		neigh = []
		for i in xrange(0,3):
			for j in xrange(0,3):
				newRow = (row - 1) + i
				newCol = (col - 1) + j
				if ((newRow>=0 and newRow<4) and (newCol>=0 and newCol<4)):	# Checks if possible coords are with the board
					neigh.append([newRow,newCol])
		return neigh

	def isWord(self,inWord):
		left = 0
		right = len(self.dictionary)

		while (left <= right):						# Binary search through alphabetized list of words
			middle = (left + right)/2
			if( inWord > self.dictionary[middle] ):
				left = middle + 1
			elif( inWord < self.dictionary[middle] ):
				right = middle - 1
			else:
				return True

		return False

	def wordSearch(self,x,y,testWord):					# self: this game instance, x,y: boardcoords, testword: word formed so far
		#print testWord
		if(len(testWord)>2):						# minimum word length: 3
			if(self.isWord(testWord)):				
				if testWord not in self.solvedWords:		
					self.solvedWords.append(testWord)
		if(len(testWord)>7):  						# MAX_WORD_LENGTH
			return						
		testWord += self.boggleBoard[x][y]					# Adds the current sqr's letter to testWord
		temp = self.boggleBoard[x][y]						# Stores current sqr's letter
		self.boggleBoard[x][y] = ''						# Erases the Letter from the board
		neighbors = self.getNeighbors(x,y)				# Gets a list of legal sqrs around current sqr
		for p in xrange(0,len(neighbors)):				# Set a loop through all neighbor sqrs		
			a = neighbors[p][0]					# Gets the pth neighbor sqr's x coord
			s = neighbors[p][1]					# Gets the pth neighbor sqr's y coord
			if (len(self.boggleBoard[a][s])>0):				# Checks that neighbor's sqr isn't already used in word
				self.wordSearch(a,s,testWord)			# recursive call with a neighbor's sqr
		self.boggleBoard[x][y] = temp						# Restores Letter for use in diffrent path


	def playGame(self):						# Start a Game

		f = open ('sowpods.txt','r')

		for line in f:
			self.dictionary.append(line.rstrip('\r\n'))	# Load dictionary

		f.close()						

		for l in xrange(0,4):
			for k in xrange(0,4):
				self.wordSearch(l,k,'')			# Start a recrusive search on each sqr of the board
				self.printBoard()

		words = self.solvedWords				# Get all sloved words from self
		
		return sorted(words)					# Return all possible words on board
