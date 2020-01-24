# Insertion Sort

# Arrange data in Ascending Order
def insertionSort(data):
    for i in range(1, len(data)):

        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1

        data[j + 1] = key


numbers = [45, 22, 11, 23, 19, 10, 33, 12, 55, 66]
insertionSort(numbers)

for number in numbers:
    print(number, end=" ")
