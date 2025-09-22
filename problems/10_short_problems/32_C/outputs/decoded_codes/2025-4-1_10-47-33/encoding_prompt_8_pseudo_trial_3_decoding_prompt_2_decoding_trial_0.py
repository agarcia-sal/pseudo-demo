def RoundUpIfNecessary(quantity, size):
    # Perform integer division to find how many complete sizes fit in the quantity
    completeSizes = quantity // size
    remainder = quantity % size
    
    # If there is a remainder, more than one size is needed for that quantity 
    if remainder > 0:
        return remainder * (completeSizes + 1)  # Calculate the effective total when rounding up
    else:
        return quantity  # No rounding needed, return the original quantity

# Get inputs from user
totalA = int(input())
totalB = int(input())
size = int(input())

# Calculate the rounded values for both quantities
roundedA = RoundUpIfNecessary(totalA, size)
roundedB = RoundUpIfNecessary(totalB, size)

# Multiply the rounded quantities together and display the result
print(roundedA * roundedB)
