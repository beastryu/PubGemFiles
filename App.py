import sys
import os
import random
from scipy import stats
from collections import Counter
import collections
import openpyxl
import gem_modules as f

DC = 0
searchType = "gemstones"
hoursSpent = 5
numberFound = 10
priceTotal = 0
pref = "Duvals"
outputArray = []

#Asking for the user inputs
'''
while __name__ == '__main__':
	gemInput = input("Were you looking for Hardstones or Gemstones?").lower()
	if 'g' in gemInput:
		searchType = "gemstones"
		break
	elif 'h' in gemInput:
		searchType = "hardstones"
		break
	elif 1 == 1:
		print("Im sorry. You need to enter a vaild gemtype.")

hoursSpent = int(input("How many hours did you spend?"))
'''


#Code for finding gemstones

if searchType == "gemstones":
	allGems = f.GemClass()
	instanceNames = allGems.allGemValues.keys()
	gemObjs = {rarity: f.gemRarityClass(rarity=rarity) for rarity in instanceNames}
	
	#More input
	'''
	print("Underground: -5 \nMountains: -4 \nRiver: -3 \nMountainous Region: -2\nDesert: -2\nJungle: -2\nCoastal Area: -1\nForest: +1\nArctic Region: +2 \nInside city walls: +3 \nInside most buildings: +5")
	DC = input("What is the DC modifier?(Subtract your proficiency bonus here, the base is 15.)")
	pref = input("And whose gems preference list are we using?")
	'''

	#Load Preference Sheet

	prefSheet = (pref + "PreferenceList.xlsx")
	wb_prefSheet = openpyxl.load_workbook(prefSheet)
	sheet_prefSheet = wb_prefSheet.active
	
	#Populate all the lists

	for obj in gemObjs:
		f.popClass(gemObjs[obj], sheet_prefSheet)
	print(gemObjs['Legendary'].deque)
