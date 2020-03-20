import math


f = open("data.txt", "r")


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
        

# Input Prompt for an alpha value
alpha = input("Enter alpha value in decimal format between 0 and 1, exclusive (0.66666 or 0.75): ")
    
    
# Main program
for x in f:
    numList = [int(n) for n in x.split(' ')]
    numsToBeSorted = numList[1:]
    badSort(numsToBeSorted, 0, len(numsToBeSorted) - 1, alpha)
    
    fout = open("bad.out", "a")
    fout.write(' '.join(str(i) for i in numsToBeSorted))
    fout.write('\n')
    fout.close()
