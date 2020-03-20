import random
import time


def merge(left, right, arr):
    leftIndex = rightIndex = arrIndex = 0
    
    while leftIndex < len(left) and rightIndex < len(right):
        if (left[leftIndex] < right[rightIndex]):
            arr[arrIndex] = left[leftIndex]
            leftIndex += 1
        else:
            arr[arrIndex] = right[rightIndex]
            rightIndex += 1
            
        arrIndex += 1
    
    while leftIndex < len(left):
        arr[arrIndex] = left[leftIndex]
        leftIndex += 1
        arrIndex += 1
    
    while rightIndex < len(right):
        arr[arrIndex] = right[rightIndex]
        rightIndex += 1
        arrIndex += 1

def mergeSort(arr, length):
    if length == 1:
        return
    
    mid = length // 2
    left = arr[:mid]
    right = arr[mid:]
    
    mergeSort(left, len(left))
    mergeSort(right, len(right))
    
    merge(left, right, arr)

def testTime(n, worst):
    numList = [i for i in range(n)]
    if worst:
        numList.reverse()
        
    startTime = time.time()
    mergeSort(numList, n)
    endTime = time.time()
    calculatedTime = endTime - startTime
    
    return calculatedTime    

caseList = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]

#Best-case
for case in caseList:
    tryNum = 1
    totalTime = 0
    for i in range(tryNum):
        totalTime += testTime(case, False)
    avgTime = totalTime / tryNum
    
    print("{},{}".format(case, avgTime))
    
#Worst-case
for case in caseList:
    tryNum = 1
    totalTime = 0
    for i in range(tryNum):
        totalTime += testTime(case, True)
    avgTime = totalTime / tryNum
    
    print("{},{}".format(case, avgTime))