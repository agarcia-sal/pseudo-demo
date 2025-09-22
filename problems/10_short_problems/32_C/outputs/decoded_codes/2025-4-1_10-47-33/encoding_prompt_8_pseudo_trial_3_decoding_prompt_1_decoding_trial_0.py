def round_up_if_necessary(quantity, size):
    # Perform integer division to find how many complete sizes fit in the quantity
    complete_sizes = quantity // size
    remainder = quantity % size
    
    # If there is a remainder, more than one size is needed for that quantity
    if remainder > 0:
        return remainder * (complete_sizes + 1)  # Calculate the effective total when rounding up
    else:
        return quantity  # No rounding needed, return the original quantity

# Get inputs from user
totalA = int(input())
totalB = int(input())
size = int(input())

# Calculate the rounded values for both quantities
roundedA = round_up_if_necessary(totalA, size)
roundedB = round_up_if_necessary(totalB, size)

# Multiply the rounded quantities together and display the result
print(roundedA * roundedB)
