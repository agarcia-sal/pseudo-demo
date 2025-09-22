def CalculateRemainderAndAdjust(total, divisor):
    # Calculate quotient and remainder using integer division and modulus
    quotient = total // divisor  # Integer division to get quotient
    remainder = total % divisor   # Modulus operation to get remainder
    
    # Adjust the output based on the presence of a remainder
    if remainder > 0:
        return remainder * (quotient + 1)  # Adjust output if there is a remainder
    else:
        return total  # Return total if there is no remainder

# Read the input values for totalA, totalB, and divisor
totalA = int(input())  # Input for the first total
totalB = int(input())  # Input for the second total
divisor = int(input())  # Input for the divisor

# Calculate the adjusted values for totalA and totalB using the divisor
adjustedValueA = CalculateRemainderAndAdjust(totalA, divisor)
adjustedValueB = CalculateRemainderAndAdjust(totalB, divisor)

# Calculate the final result by multiplying the two adjusted values
finalResult = adjustedValueA * adjustedValueB

# Output the final result
print(finalResult)
