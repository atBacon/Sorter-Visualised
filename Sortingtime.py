numbersList = []
sortedNList = []
normList = []
#Needed to create a "normal list" to make old list shower work
lowNPlace = 0
lowNSize = 101
import random
import matplotlib.pyplot as plt
import numpy as np

for i in range (100):
    normList.append(i)
    numbersList.append(random.randrange(0,100))

#show old list 
plt.bar(normList, numbersList)
plt.pause(0.001)
plt.clf
    
#for i in range (len(numbersList)):

#I know it's a comically inefficent sorting algorithm

for i in range (100):
    for x in numbersList:
        if (x) < lowNSize:
            lowNSize = x
            lowNPlace = numbersList.index(lowNSize)
    sortedNList.append(lowNSize)
    numbersList.pop(lowNPlace)
    #Delete smallest number from old list and add it to new
    
#show new list    
    plt.bar(len(sortedNList), sortedNList)
    plt.pause(0.001)
    plt.clf
#reset variables    
    lowNPlace = 0
    lowNSize = 101
