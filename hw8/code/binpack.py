import math


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
            
    print("First-Fit: {}".format(len(bins)))
    # print("bins: ", bins)
    
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
            
    print("First-Fit-Decreasing: {}".format(len(bins)))
    # print("bins: ", bins)

    
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
    
    print("Best-Fit: {}".format(len(bins)))
    # print("bins: ", bins)



def main():
    with open('bin.txt') as f:
        n = int(f.readline()) # number of cases
        
        # Run multiple cases
        for x in range(n):
            c = int(next(f)) # capacity of bins
            n = int(next(f)) # number of items
            items = [int(elem) for elem in next(f).split(' ')] # list of items
            lowerBound = int(math.ceil(sum(items) / c)) # total weight of items / c
            
            print("Test Case {}".format(x+1))
            firstFit(items, c, lowerBound)
            firstFitDecreasing(items, c, lowerBound)
            bestFit(items, c)
            print("-----------------------------------")
            
if __name__ == '__main__':
   main()
