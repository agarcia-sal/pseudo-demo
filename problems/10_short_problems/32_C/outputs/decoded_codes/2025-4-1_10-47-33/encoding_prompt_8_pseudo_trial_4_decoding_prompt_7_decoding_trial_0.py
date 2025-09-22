def AdjustQuantity(quantity, divisor):
    # Calculate how many full groups can be made from the quantity
    fullGroups = quantity // divisor  # Integer division
    remainder = quantity % divisor      # Remainder after division

    # If there is a remainder, adjust the quantity
    if remainder > 0:
        return remainder * (fullGroups + 1)
    else:
        return quantity  # No adjustment needed if no remainder


# Begin Main Program
# Read input of three integers n, m, and s
inputLine = input()  # Read a single line of input
n, m, s = map(int, inputLine.split())  # Convert the input line into integers

# Adjust the quantities using the AdjustQuantity function
adjustedN = AdjustQuantity(n, s)
adjustedM = AdjustQuantity(m, s)

# Calculate the product of the adjusted quantities
result = adjustedN * adjustedM

# Print the resulting product
print(result)
