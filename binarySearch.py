# def binSearch(numbers, element):
#     low = 0
#     length = len(numbers)
#     # print(length)
#     high = length - 1
#     mid = numbers[int((length-1)/2)]
#
#     if element < numbers[mid]:
#         numbers = numbers[:mid]
#
#     if element > numbers[mid]:
#         numbers = numbers[mid:]
#
#     if element == numbers[mid-1]:
#         return True
#
# print(binSearch(numbers, element))



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 5

low = 0
length = len(numbers)
# print(length)
high = length - 1

def binSearch(numbers,low,high, element):

    mid = low + (high - low)//2


    if numbers[mid] == element:
        return True

    if numbers[mid] < element:
        # low = mid+1
        return binSearch(numbers, mid+1, high, element)


    if numbers[mid] > element:
        # high = mid-1
        return binSearch(numbers, low, mid-1, element)


print(binSearch(numbers,low, high, element))