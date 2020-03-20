f = open("data.txt", "r")

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

for x in f:
    numList = [int(n) for n in x.split(' ')]
    length = int(numList[0])
    numsToBeSorted = numList[1:]
    
    mergeSort(numsToBeSorted, length)
    
    fout = open("merge.out.txt", "a")
    fout.write(' '.join(str(i) for i in numsToBeSorted))
    fout.write('\n')
    fout.close()