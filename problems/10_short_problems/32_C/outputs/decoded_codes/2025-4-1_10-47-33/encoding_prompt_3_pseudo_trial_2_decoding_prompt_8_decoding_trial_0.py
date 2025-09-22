def CalculateRemainderCountAndMultiply(inputValue1, inputValue2, divisor):
    quotient = inputValue1 // divisor
    remainder = inputValue1 % divisor
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return inputValue1

# Start Main Program
inputValue1 = int(input())
inputValue2 = int(input())
divisor = int(input())

result1 = CalculateRemainderCountAndMultiply(inputValue1, inputValue2, divisor)
result2 = CalculateRemainderCountAndMultiply(inputValue2, divisor)

finalResult = result1 * result2
print(finalResult)


def CalculateRemainderCountAndMultiply(inputValue1, inputValue2, divisor):
    """Calculates modified remainder based on inputValue1 and divisor."""
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    
    quotient = inputValue1 // divisor
    remainder = inputValue1 % divisor
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return inputValue1
