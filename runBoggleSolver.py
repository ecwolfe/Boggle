#!/usr/bin/python

import Boggle

b=Boggle.Boggle()
b.clearWordList()
bboard=b.getBoard()
b.printBoard()
solutions =b.playGame()
print solutions
