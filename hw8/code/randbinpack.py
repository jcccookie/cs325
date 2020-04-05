import math
import random

def getSpace(bins, c):
    total = 0
    
    for b in bins:
        total += c-b
    
    return total

def firstFit(items, c, lowerBound):
    bins = [0 for x in range(lowerBound)]
    
    for item in items:
        isItemChecked = False
        for i in range(len(bins)):
            if item + bins[i] <= c:
                bins[i] += item
                isItemChecked = True
                break
        if not isItemChecked:
            bins.append(item)
            
    leftSpace = getSpace(bins, c)
            
    print("First-Fit: {}".format(len(bins)))
    print("bins: {}, {}\n".format(bins, leftSpace))
    # print("Total space left: {}\n".format(leftSpace))
    
def firstFitDecreasing(items, c, lowerBound):
    bins = [0 for x in range(lowerBound)]
    sortedItem = sorted(items, reverse = True)
    
    for item in sortedItem:
        isItemChecked = False
        for i in range(len(bins)):
            if item + bins[i] <= c:
                bins[i] += item
                isItemChecked = True
                break
        if not isItemChecked:
            bins.append(item)
            
    leftSpace = getSpace(bins, c) 
            
    print("First-Fit-Decreasing: {}".format(len(bins)))
    print("bins: {}, {}\n".format(bins, leftSpace))
    # print("Total space left: {}\n".format(leftSpace))

    
def bestFit(items, c):
    bins = []
    
    for item in items:
        # Find the bin with the tightest space that fits to item
        ti = -1 # tightest index
        minRoomInBin = c
        
        for i in range(len(bins)):
            if bins[i]+item <= c and c-bins[i] <= minRoomInBin:
                minRoomInBin = c-bins[i]
                ti = i
        
        if ti >= 0:
            bins[ti] += item
        else:
            bins.append(item)
            
    leftSpace = getSpace(bins, c)
    
    print("Best-Fit: {}".format(len(bins)))
    print("bins: {}, {}\n".format(bins, leftSpace))
    # print("Total space left: {}\n".format(leftSpace))


def main():
    for i in range(30):
        c = random.randint(10, 20) # random capacity of bins 1 <= c <= 10
        items = [random.randint(1, c) for x in range(random.randint(1, 30))] # list of items
        n = len(items)
        lowerBound = int(math.ceil(sum(items) / c)) # total weight of items / c
        
        print("Test Case {}".format(i+1))
        print("Items: {}".format(items))
        print("c: {}, n: {}, lowerBound: {}\n".format(c, n, lowerBound))
        firstFit(items, c, lowerBound)
        firstFitDecreasing(items, c, lowerBound)
        bestFit(items, c)
        print("-----------------------------------")
            
if __name__ == '__main__':
   main()
