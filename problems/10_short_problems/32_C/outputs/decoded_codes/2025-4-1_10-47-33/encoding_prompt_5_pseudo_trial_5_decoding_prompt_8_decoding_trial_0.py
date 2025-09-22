def CalculateRemainderAndAdjust(total, divisor):
    quotient = total // divisor
    remainder = total % divisor
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total

# Read input values
totalA = int(input())
totalB = int(input())
divisor = int(input())

# Calculate the adjusted values for totalA and totalB using divisor
adjustedValueA = CalculateRemainderAndAdjust(totalA, divisor)
adjustedValueB = CalculateRemainderAndAdjust(totalB, divisor)

# Calculate the final result by multiplying the two adjusted values
finalResult = adjustedValueA * adjustedValueB

# Output the final result
print(finalResult)
