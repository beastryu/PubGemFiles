import sys
import os
import random
from scipy import stats
from collections import Counter
import collections
import openpyxl
import gem_modules as f

def weighted_choices(w, mu, sd, *, k=1):
        weights = stats.norm(mu, sd).pdf(range(len(w)))
        return random.choices(w, weights=weights, k=k)

fullSheet = ("GemList.xlsx")
wb_fullSheet = openpyxl.load_workbook(fullSheet)
gemSheet = wb_fullSheet.active
prefSheet = ("DuvalsPreferenceList.xlsx")
wb_prefSheet = openpyxl.load_workbook(prefSheet)
sheet_prefSheet = wb_prefSheet.active

allGems = f.GemClass()
instanceNames = allGems.allGemValues.keys()
#Still dont understand why the interator can be called block of code
gemObjs = {rarity: f.gemRarityClass(rarity=rarity) for rarity in instanceNames}

gemObjs['Uncommon'].count = 10

def randomDice(array, number):
	for i in range(number):
		num =  0
		num += (random.randint(1, 20) + random.randint(1, 20) + random.randint(1, 4))
		array.append(num)

def makeNumberArray(array, number):
	for i in range(number): array.append(i + 1) 

testArray = []
numberArray = []
makeNumberArray(numberArray, 42)
print(numberArray)

randomDice(testArray, 1000000)
diceCnt = Counter(testArray)
print(diceCnt.most_common(6))
mvsM, mvsV, msvStd = stats.mvsdist(testArray)
mean, var, skew, kurt = stats.norm.stats(testArray, moments='mvsk')
#var = stats.norm.stats(testArray, moments='k')
#print(std.std())




'''
weightedArray = []
for i in range(44):
	weightedArray.append(i+1)

funcCnt = Counter(weighted_choices(weightedArray, 22.5, 5, k=10))
'''


'''
obj = gemObjs['Uncommon']

f.popClass(obj, sheet_prefSheet)
f.result(obj)
funcCnt = Counter(weighted_choices(obj.deque, obj.midPoint, 5, k=10))
print(funcCnt)



instanceNames = allGems.allGemValues.keys()
# Here you use the dictionary
holder = {rarity: f.gemRarityClass(rarity=rarity) for rarity in instanceNames}

LegendaryC = f.gemRarityClass("Legendary")

allGems = f.GemClass()
instanceNames = allGems.allGemValues.keys()
print(instanceNames)


f.popClass(LegendaryC, sheet_prefSheet)
f.popClass(holder['Legendary'], sheet_prefSheet)


gemCounter = Counter(holder['Legendary'].deque)
prefCounter = Counter(LegendaryC.deque)
print(sum(gemCounter.values()))
print(sum(prefCounter.values()))
print(LegendaryC.deque)
print(holder['Legendary'].deque)
'''