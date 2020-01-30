numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 7

isElementFound = False

for i in range(0, len(numbers)):
    if numbers[i] == element:
        isElementFound = True
        break

if isElementFound:
    print("Element found", numbers[i])
else:
    print("Element not found", numbers[i])