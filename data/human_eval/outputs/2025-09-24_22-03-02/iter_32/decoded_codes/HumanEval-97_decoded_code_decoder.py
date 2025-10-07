def multiply(a, b):
    remainderA = a % 10
    absoluteRemainderA = abs(remainderA)
    remainderB = b % 10
    absoluteRemainderB = abs(remainderB)
    product = absoluteRemainderA * absoluteRemainderB
    return product