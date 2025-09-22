def CalculateRemainderDistribution(totalItems, segmentSize):
    # Divide total items by segment size to get number of full segments and the remainder
    fullSegments = totalItems // segmentSize   # Integer division
    remainder = totalItems % segmentSize        # Modulus operation

    # If there is a remainder, calculate additional items; otherwise, return total items
    if remainder > 0:
        return remainder * (fullSegments + 1)
    else:
        return totalItems

# Read input values for total items n and m, and segment size s
totalItemsN = int(input())
totalItemsM = int(input())
segmentSize = int(input())

# Calculate the distribution for totalItemsN and totalItemsM using the segmentSize
resultN = CalculateRemainderDistribution(totalItemsN, segmentSize)
resultM = CalculateRemainderDistribution(totalItemsM, segmentSize)

# Output the product of the two results
print(resultN * resultM)
