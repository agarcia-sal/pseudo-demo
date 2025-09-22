def CalculateRemainderAndAdjust(total, divisor):
    # Divide total by divisor to get quotient and remainder
    quotient = total // divisor
    remainder = total % divisor
    
    # If there is a remainder, adjust the output; otherwise, return the total
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
