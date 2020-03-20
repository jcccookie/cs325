f = open("data.txt", "r")

def insertionSort(arr, length):
    for j in range(1, length):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

for x in f:
    numList = [int(n) for n in x.split(' ')]
    length = int(numList[0])
    numsToBeSorted = numList[1:]
    insertionSort(numsToBeSorted, length)
    
    fout = open("insert.out.txt", "a")
    fout.write(' '.join(str(i) for i in numsToBeSorted))
    fout.write('\n')
    fout.close()