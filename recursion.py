# def rec(num):
#
#     if num>0:
#         print(num)
#         rec(num-1)
#
# rec(10)

# def numToBin(num1):
#     if num1 > 0:
#         a = num1//2
#         print(num1%2, end=" ")
#         numToBin(a)
#         # numToBin(int(a))
#
#
# numToBin(8)


def maxNum(data, a):

    if a == 1:
        return data[0]
    else:
        num2 = maxNum(data, a-1)

    if num2> data[a-1]:
        return num2
    else:
        return data[a-1]

numbers = [10, 12, 32, 11, 34, 5]
print(maxNum(numbers, len(numbers)))