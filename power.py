def power(x, y):
    result = 1                      #1
    for i in range (0,y):           #y times
        result *= x                 #1

    return result;                  #1

print(power(2, 5))
# the above method takes linear time... (T = n+2)

