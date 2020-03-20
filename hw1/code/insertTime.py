import random
import time


def insertionSort(arr, length):
    for j in range(1, length):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

def testTime(n):
    numRange = 10000
    numList = [random.randint(0, numRange) for i in range(n)]
    
    startTime = time.time()
    insertionSort(numList, n)
    endTime = time.time()
    calculatedTime = endTime - startTime
    
    return calculatedTime
    

caseList = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]

for case in caseList:
    tryNum = 3
    totalTime = 0
    for i in range(tryNum):
        totalTime += testTime(case)
    avgTime = totalTime / tryNum
    
    print("n: {}, time: {}".format(case, avgTime))
    
