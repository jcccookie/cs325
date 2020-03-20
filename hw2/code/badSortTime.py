import math
import random
import time


def badSort(A, low, high, alpha):
    n = high - low + 1
    if n == 2 and A[low] > A[high]:
        A[low], A[high] = A[high], A[low]
    elif n > 2:        
        m = int(math.ceil(alpha * n))
        if m == n and m > 2:
            m = n - 1        
        badSort(A, low, low+m-1, alpha)
        badSort(A, high-m+1, high, alpha)
        badSort(A, low, low+m-1, alpha)
        
        
def testTime(n):
    numRange = 10000
    numList = [random.randint(0, numRange) for i in range(n)]
    
    startTime = time.time()
    badSort(numList, 0, n-1, 0.6666667)
    # badSort(numList, 0, n-1, 0.75)
    endTime = time.time()
    calculatedTime = endTime - startTime
    
    return calculatedTime    

caseList = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]

for case in caseList:
    tryNum = 1
    totalTime = 0
    for i in range(tryNum):
        totalTime += testTime(case)
    avgTime = totalTime / tryNum
    
    print("n: {}, time: {}".format(case, avgTime))