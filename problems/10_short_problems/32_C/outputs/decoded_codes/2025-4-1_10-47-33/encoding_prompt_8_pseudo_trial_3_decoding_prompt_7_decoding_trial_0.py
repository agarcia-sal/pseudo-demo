def CalculateRoundedProduct():
    # Define a function to calculate rounded quantity
    def RoundUpIfNecessary(quantity, size):
        # Perform integer division to find how many complete sizes fit in the quantity
        completeSizes = quantity // size
        remainder = quantity % size
        
        # If there is a remainder, more than one size is needed for that quantity 
        if remainder > 0:
            # Calculate the effective total when rounding up
            return (remainder * (completeSizes + 1))
        else:
            # No rounding needed, return the original quantity
            return quantity

    # Get inputs from user
    totalA = int(input())  # Represents 'n'
    totalB = int(input())  # Represents 'm'
    size = int(input())     # Represents 's'
    
    # Calculate the rounded values for both quantities
    roundedA = RoundUpIfNecessary(totalA, size)
    roundedB = RoundUpIfNecessary(totalB, size)

    # Multiply the rounded quantities together and display the result
    print(roundedA * roundedB)

# Call the function to execute the program
CalculateRoundedProduct()
