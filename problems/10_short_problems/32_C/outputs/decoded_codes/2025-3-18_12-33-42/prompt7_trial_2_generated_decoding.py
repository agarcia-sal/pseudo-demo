def calculateRemainderAndAdjust(quantity, divisor):
    # Calculate how many full sets of 'divisor' fit into 'quantity'
    fullSetsCount = quantity // divisor
    remainder = quantity % divisor
    
    # If there is a remainder, adjust the result
    if remainder > 0:
        return remainder * (fullSetsCount + 1)  # Adjust for the partial set
    else:
        return quantity  # No adjustment needed

# Main program begins here
# Read values for quantityN, quantityM, and divisorS
quantityN = int(input())
quantityM = int(input())
divisorS = int(input())

# Calculate adjusted results for both quantities
adjustedResultN = calculateRemainderAndAdjust(quantityN, divisorS)
adjustedResultM = calculateRemainderAndAdjust(quantityM, divisorS)

# Output the product of the two adjusted results
print(adjustedResultN * adjustedResultM)
