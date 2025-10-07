def multiply(a, b):
    remainderA = a % 10
    if remainderA < 0:
        remainderA = remainderA * -1
    remainderB = b % 10
    if remainderB < 0:
        remainderB = remainderB * -1
    product = remainderA * remainderB
    return product