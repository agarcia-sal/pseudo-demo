def AdjustQuantity(quantity, divisor):
    fullGroups = quantity // divisor
    remainder = quantity % divisor
    if remainder > 0:
        return remainder * (fullGroups + 1)
    else:
        return quantity

# Begin Main Program
inputLine = input()
n, m, s = map(int, inputLine.split())
adjustedN = AdjustQuantity(n, s)
adjustedM = AdjustQuantity(m, s)
result = adjustedN * adjustedM
print(result)
