def AdjustQuantity(quantity, divisor):
    # Calculate how many full groups can be made from the quantity
    fullGroups = quantity // divisor
    remainder = quantity % divisor

    # If there is a remainder, return adjusted quantity
    if remainder > 0:
        return remainder * (fullGroups + 1)
    else:
        # No adjustment needed, return original quantity
        return quantity

# Main Program Execution
inputLine = input()  # Read a single line of input
n, m, s = map(int, inputLine.split())  # Convert to integers 

adjustedN = AdjustQuantity(n, s)  # Adjust n
adjustedM = AdjustQuantity(m, s)  # Adjust m

result = adjustedN * adjustedM  # Calculate the product
print(result)  # Print the resulting product
