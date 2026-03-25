def fact(n):
    result = 1
    #RANGE FROM ( 1 TO N + 1): 1 TO 1+1 , 2 TO 2 + 1 , 3 TO 3 + 1 ETC....
    for i in range(1, n + 1):
    # ASSIGN THE RESULT WITH ITSELF : RESULT = RESULT * I
        result *= i
    return result

print(fact(28))