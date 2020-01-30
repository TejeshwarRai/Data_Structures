def getMinIdx(data, start, stop):
    minIdx = start

    for i in range(start, stop):
        if data[i] < data[minIdx]:
            minIdx = i

    return minIdx


def swapElements(data, i, j):
    data[i], data[j] = data[j], data[i]


def selectionSort(data):
    for i in range(0, len(data)):
        minIdx = getMinIdx(data, i, len(data))
        # print(">> Minimum Index is", minIdx)
        swapElements(data, minIdx, i)
    print(data)

print("SELECTION SORT")
numbers = [45, 22, 11, 23, 19, 10, 33, 12, 55, 66]
print(numbers)
selectionSort(numbers)
