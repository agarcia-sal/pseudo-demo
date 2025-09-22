def CalculateModifiedCount(TotalItems, GroupSize):
    # Divide TotalItems by GroupSize
    Quotient, Remainder = divmod(TotalItems, GroupSize)

    # Check if there is a remainder
    if Remainder > 0:
        return Remainder * (Quotient + 1)  # Include partial group adjustments
    else:
        return TotalItems  # No partial groups

# Get user input
InputLine = input()
TotalItemsN, TotalItemsM, GroupSizeS = map(int, InputLine.split())

# Calculate modified counts for both total items
ModifiedCountN = CalculateModifiedCount(TotalItemsN, GroupSizeS)
ModifiedCountM = CalculateModifiedCount(TotalItemsM, GroupSizeS)

# Calculate the final product
FinalProduct = ModifiedCountN * ModifiedCountM

# Print the result
print(FinalProduct)
