#Hi
#Tesing Varibles
testArray = []
testDeque = collections.deque()

#Compare the stats functions to any dice probability
bigKCounter = collections.Counter()
bigKCounter.update(random.choices(testDeque, weights = dWeights, k=1000000))
print(bigKCounter)

#Condensed into a function
for i in range(numberFound):
    gemFound = weighted_choices(CommonClass.deque, CommonClass.midPoint, 8.9, k=1000)
    weightedCounter.update(gemFound)

#Weights for the common class
dWeights = collections.defaultdict(int)

dWeights = [0.025,
0.075,
0.15,
0.25,
0.375,
0.525,
0.7,
0.9,
1.125,
1.375,
1.625,
1.875,
2.125,
2.375,
2.625,
2.875,
3.125,
3.375,
3.625,
3.875,
4.075,
4.225,
4.325,
4.375,
4.375,
4.325,
4.225,
4.075,
3.875,
3.625,
3.375,
3.125,
2.875,
2.625,
2.375,
2.125,
1.875,
1.625,
1.375,
1.125,
0.9,
0.7,
0.525,
0.375,
0.25,
0.15,
0.075,
0.025]
