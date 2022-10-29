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

allGems = f.GemClass()
instanceNames = allGems.allGemValues.keys()
gemObjs = {rarity: f.gemRarityClass(rarity=rarity) for rarity in instanceNames}

for i in range(numberFound):
    rarity = random.randint(1, 20)
    if rarity <= 6: 
        gemObjs['Common'].countUp()
    elif rarity >= 7 and rarity <= 11:
        gemObjs['Uncommon'].countUp()
    elif rarity >= 12 and rarity <= 15:
        gemObjs['Rare'].countUp()
    elif rarity >= 16 and rarity <= 18:
        gemObjs['VeryRare'].countUp()
    elif rarity >= 19:
        gemObjs['Legendary'].countUp()
    else:
        print(ERROR)


prefSheet = (pref + "PreferenceList.xlsx")
wb_prefSheet = openpyxl.load_workbook(prefSheet)
sheet_prefSheet = wb_prefSheet.active



f.popClass(gemObjs['Common'], sheet_prefSheet)
print('Test Deque \n' + str(gemObjs['Common'].deque))

print('MidPoint: ' + str(gemObjs['Common'].midPoint))


print(Counter(f.result(gemObjs['Common'])))



##creating containers
weightedCounter = collections.Counter()
keyVCounter = collections.Counter()


'''
print('Out of ' + str(numberFound) + '\n')
print('Gaussion distribution\n' + str(weightedCounter) + '\n')
print('Key Value probability\n' + str(keyVCounter))

print("\n \n top 5 for weightedCounter" + str(weightedCounter.most_gemObjs['common'](10)))
print("\n \n top 5 for keyVCounter" + str(keyVCounter.most_gemObjs['common'](10)) + '\n')


print(weightedCounter)
print(keyVCounter)


# Tally occurrences of words in a list
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)
'''